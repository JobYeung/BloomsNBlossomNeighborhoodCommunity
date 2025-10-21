from django.db import models
from datetime import datetime

class Contact(models.Model):
    product = models.CharField(max_length=200)
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,blank=True)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now,blank=False)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    