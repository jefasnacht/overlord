from django.db import models


class Feature(models.Model):
    feature_name = models.CharField(max_length=200)
    discover_date = models.DateTimeField('date published')


class Choice(models.Model):
    feature = models.ForeignKey(Feature)
    feature_text = models.CharField(max_length=200)
    lat = models.IntegerField(default=0)
    lon = models.IntegerField(default=0)
