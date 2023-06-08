from django.db import models


# Create your models here.
class Spravka(models.Model):
    fio = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    grant = models.IntegerField()
    destination = models.CharField(max_length=100)

