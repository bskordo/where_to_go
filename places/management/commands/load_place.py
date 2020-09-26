from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import requests
import json
from places.models import Place, Photo
from PIL import Image as Img
from io import BytesIO
from django.core.files.base import ContentFile
import logging
logger = logging.getLogger('Logger')


class Command(BaseCommand):
    help = 'Create place'

    def is_server_response_correct(self, response):
        return response.ok and 'error' not in response.json()

    def add_arguments(self, parser):
        parser.add_argument('site_url', type=str, help='site url with place description')

    def insert_into_place_table(self, data):
        place, not_created = Place.objects.get_or_create(title=data['title'],
            description_short=data['description_short'],
            longitude=data['coordinates']['lng'],
            latitude=data['coordinates']['lat'],
            description_long=data['description_long'])
        if not_created:
            images = data['imgs']
            for img in images:
                response = requests.get(img)
                self.insert_into_image_table(response.content, place)

    def insert_into_image_table(self, content, place_title):
        photos = Photo(place=place_title)
        img_content = ContentFile(content)
        photos.photo.save('myphoto.jpg', img_content, save=True)

    def handle(self, *args, **kwargs):
        url = kwargs['site_url']
        response = requests.get(url)
        if self.is_server_response_correct(response):
            json_data = json.loads(response.text)
            self.insert_into_place_table(json_data)
        else:
            logger.error('Received Bad response')
