from cffi import model
from django.contrib.gis.geometry.backend import module
from django.db import models

# Create your models here.
from werkzeug import module


class Department(models.Model):
    department = models.CharField(max_length=56)

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    age = models.IntegerField(null=True)
    dep = models.ForeignKey('Department',null=True)

class User(models.Model):
    user = models.CharField(max_length=32,null=False)
    phone = models.BigIntegerField(null=False)
    password = models.CharField(max_length=128,null=False)

# class employee(models.Model):



