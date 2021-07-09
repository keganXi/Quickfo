from django.db import models
from django.utils import timezone

# Create your models here.


class FoxSportsDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class TheGuardianDatabase(models.Model):

    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class BBCSportsDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class TheIndependentDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


