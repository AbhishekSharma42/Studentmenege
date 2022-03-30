from pyexpat import model
from django.db import models

# Create your models here.

class Student(models.Model):
    stuName=models.CharField(max_length=20)
    stuMob=models.CharField(max_length=10)
    stuEmail=models.EmailField()
    bran=models.CharField(max_length=5,default="")
    
class IntrestStu(models.Model):
    stuName=models.CharField(max_length=20)
    stuMob=models.CharField(max_length=10)
    stuEmail=models.EmailField()
    bran=models.CharField(max_length=5,default="")