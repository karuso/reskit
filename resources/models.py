from django.db import models

class Resource(models.Model):
    
    name = models.CharField(max_length=80)
    cal_link = models.TextField()
