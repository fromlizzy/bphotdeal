from django.db import models

# Create your models here.


class Deal(models.Model):
    thumb_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True)
    price = models.CharField(max_length=200)
    discount = models.IntegerField()
