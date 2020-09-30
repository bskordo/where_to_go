import json

from .models import Photo
from .models import Place
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


def place_details(request, pk):
    place = get_object_or_404(Place, pk=pk)
    photos = place.place_photo.all()
    place_details = {
        'title': place.title,
        'imgs': [photo.photo.url for photo in photos],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude}}
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
