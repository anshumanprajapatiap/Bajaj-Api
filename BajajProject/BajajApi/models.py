from django.db import models

# Create your models here.
class Details(models.Model):
    #john_doe_17091999
    name = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.name
