from django.db import models

# Create your models here.

class HouseModel(models.Model):


    name = models.CharField(max_length= 50)
    location = models.CharField(max_length=50)
    square_feet = models.IntegerField()
    Bath = models.IntegerField()
    BHK = models.IntegerField()


    def __str__(self):

        return self.name
