from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class Place(models.Model):
    title = models.CharField("Название", max_length=100)
    description_short = models.TextField("Короткое описание", blank=True)
    description_long = tinymce_models.HTMLField("Полное описание", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место отдыха", related_name='place_photo')
    photo_order = models.PositiveIntegerField("Порядок фотографий", default=0)
    photo = models.ImageField("Фотографие")

    class Meta:
        ordering = ["photo_order"]

    def __str__(self):
        return '%s  %s' % (self.photo_order, self.place.title)
