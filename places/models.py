from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class Place(models.Model):
    title = models.CharField("Название место отдыха", max_length=100)
    description_short = models.CharField("Короткое описание место отдыха", max_length=200, blank=True)
    description_long = tinymce_models.HTMLField("Полное описание место отдыха", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")



class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Cвязь с местом отдыха",related_name='places')
    photo_order = models.PositiveIntegerField("Gорядок фотографий",default=0, blank=False, null=False)
    photo = models.ImageField("Фотография место отдыха")


    class Meta:
        ordering = ["photo_order"]


    def __str__(self):
        return '%s  %s'  %(self.photo_order, self.place.title)

