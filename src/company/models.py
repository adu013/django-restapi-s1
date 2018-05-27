from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    slogan = models.CharField(max_length=100)
    year_founded = models.IntegerField()

    def __str__(self):
        return self.name
