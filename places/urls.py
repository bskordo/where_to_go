from django.urls import path, include
from places import views

urlpatterns = [
    path(r'<pk>/', views.place_details, name='place_details'),
    path('tinymce/', include('tinymce.urls'))
] 