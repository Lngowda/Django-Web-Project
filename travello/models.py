from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.


class Destination(models.Model):
   
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.IntegerField()
    price = models.IntegerField()
    offer  =models.BooleanField(default=False)
