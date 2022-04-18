from django.db import models

class todo(models.Model):
    name = models.CharField(max_length=50)