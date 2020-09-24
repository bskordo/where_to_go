from django.shortcuts import render
from .models import Place, Photo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.urls import reverse


def place_details(request, id):
    place = get_object_or_404(Place, id=id)
    photos = place.place_photo.all()
    place_details = {
        'title': place.title,
        'imgs': [photo.photo.url for photo in photos],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude}}
    return HttpResponse(json.dumps(place_details, ensure_ascii=False), content_type="application/json")
