from django.db import models
from datetime import datetime
from florists.models import Florist

from taggit.managers import TaggableManager

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    florist = models.ForeignKey(Florist, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    flower_type = models.CharField(max_length=200)
    flower_style = models.CharField(max_length=200)
    occasion = models.CharField(max_length=200,default='')
    #occasion = models.ManyToManyField(Subject, blank=True)
    category = TaggableManager(verbose_name="Category")
    seasonal = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='products/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField()

    class Meta:
        ordering = ('-title',)
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

    
    def tag_list(self):
        return u", ".join(tag.name for tag in self.services.all())    