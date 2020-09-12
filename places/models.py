from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=200)
    description_long = tinymce_models.HTMLField()
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
         return '%s' % (self.title)


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    photo_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    photo = models.ImageField()


    class Meta:
        ordering = ["photo_order"]


    def __str__(self):
        return '%s  %s'  %(self.photo_order, self.place.title)

