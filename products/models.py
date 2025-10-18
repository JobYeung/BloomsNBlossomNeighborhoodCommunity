from django.db import models

class Product(models.Model):
    florist = models.ForeignKey('florists.Florist', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    flower_type = models.CharField(max_length=200)
    flower_stylee = models.CharField(max_length=200)
    seasonal = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='phots/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='phots/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField()
    def __str__(self):
        return self.title
    