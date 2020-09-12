#from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import requests
import json
from places.models import Place, Photos
from PIL import Image as Img
from io import BytesIO
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Create place '

    def add_arguments(self, parser):
        parser.add_argument('site_url', type=str, help='site url with place description')


    def get_information_from_url(self,url):
        return requests.get(url)


    def insert_into_place_table(self, data):
        place = Place(title=data['title'],description_short=data['description_short'],
            latitude=data['coordinates']['lng'],
            longitude=data['coordinates']['lat'],
            description_long=data['description_long'])
        place.save()
        images = data['imgs']
        for img in images:
            cont = self.get_information_from_url(img)
            img_cont = Img.open(BytesIO(cont.content))
            self.insert_into_image_table(cont.content, place)


    def insert_into_image_table(self, content, place_title):
        photos = Photos(title=place_title)
        img_content = ContentFile(content)
        photos.photo.save('myphoto.jpg', img_content, save=True)


    def handle(self, *args, **kwargs):
        url = kwargs['site_url']
        resp = self.get_information_from_url(url)
        json_data = json.loads(resp.text)
        self.insert_into_place_table(json_data)
