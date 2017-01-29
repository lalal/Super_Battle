from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ComicZineFighter(models.Model):
    fighter_id = models.IntegerField() 
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    publisher = models.TextField(null=True)
    image = models.TextField(null=True) 
    origin = models.TextField(null=True)
    description = models.TextField(null=True)
    deck = models.TextField(null=True)
    api_detail_url = models.TextField(null=True)
    site_detail_url = models.TextField(null=True)
    first_appeared_in_issue = models.TextField(null=True)
    count_of_issue_appearances = models.IntegerField(null=True)
    birth = models.TextField(null=True)
    real_name = models.TextField(null=True)
    aliases = models.TextField(null=True)
    date_added = models.DateTimeField(null=True)
    date_last_updated = models.DateTimeField(null=True)
