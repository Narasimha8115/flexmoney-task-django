from datetime import datetime
from django.db import models

# Create your models here.

class Yoga_Class_Data(models.Model):

    firstName = models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    fullName=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=100)
    age=models.CharField(max_length=2)
    session=models.CharField(max_length=100)
    fee=models.IntegerField(default=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = ("Yoga_Class_Data")
        verbose_name_plural = ("Yoga_Class_Datas")

    def ___str___(self):
        return self.firstName

