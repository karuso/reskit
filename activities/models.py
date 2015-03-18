from django.db import models
from resources.models import Resource

class Activity(models.Model):

    resource = models.ForeignKey(Resource)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
