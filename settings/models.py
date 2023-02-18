from django.db import models

# Create your models here.

class Company (models.Model):
    name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='company/')
    call_us = models.CharField(max_length=25)
    email_us = models.EmailField()
    subtitle = models.TextField(max_length=500)
    fb_link = models.URLField(null=True,blank=True)
    twit_link = models.URLField(null=True,blank=True)
    insta_link = models.URLField(null=True,blank=True)
    emails = models.TextField(max_length=100)
    numbers = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__ (self):
        return self.name