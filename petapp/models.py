from django.db import models

# Create your models here.
class pet_tbl(models.Model):
    pnm = models.CharField(max_length=25)
    prc= models.IntegerField() 