from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place
from django.urls import reverse


def index_page(request):
    places = Place.objects.all()
    place_features = []
    for place in places:
        place_details = {'type': 'Feature', 'geometry': {'type': 'Point',
                         'coordinates': [place.longitude, place.latitude]},
                         'properties': {'title': place.title, 'placesId': place.id,
                         'detailsUrl': reverse('place_details', args=[place.id])}}
        place_features.append(place_details)
    place_details_json = {'type': 'FeatureCollection', 'features': place_features}
    return render(request, 'index.html', context={'places': place_details_json})
