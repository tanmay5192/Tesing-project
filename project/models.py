from django.db import models
from django.core import validators


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    service=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,null=True)
    phone=models.IntegerField(null=True)
    message=models.TextField(max_length=10000,null=True)

def cleans_name(self):
    im = self.cleaned_data['name']
