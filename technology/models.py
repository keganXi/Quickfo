from django.db import models
from django.utils import timezone

# Create your models here.


class TheVergeDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class CnetDatabase(models.Model):

    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class MashableDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class RecodeDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())


class GizmodoDatabase(models.Model):
    title_entry = models.CharField(max_length=250)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())
