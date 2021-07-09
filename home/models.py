
from django.db import models
from django.utils import timezone


# Create your models here.
class TheVergeDatabase(models.Model):
    title_entry = models.CharField(max_length=200)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

    class Meta:
        get_latest_by = "date_published"


class MSNBCDatabase(models.Model):
    title_entry = models.CharField(max_length=200)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

    class Meta:
        get_latest_by = "date_published"



class XXLMagDatabase(models.Model):
    title_entry = models.CharField(max_length=200)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

    class Meta:
        get_latest_by = "date_published"



class TheIndependentDatabase(models.Model):
    title_entry = models.CharField(max_length=200)
    content_entry = models.TextField()
    media_entry = models.TextField()
    link_entry = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

    class Meta:
        get_latest_by = "date_published"







