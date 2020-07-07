from django.db import models
from django.contrib.postgres.fields import JSONField


class User(models.Model):
    name = models.CharField(max_length=255)
    sex = models.IntegerField()
    hobby = JSONField()
    money = models.DecimalField(max_digits=16, decimal_places=4)
    start_time = models.DateField()


class Us_pwd(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Ustest(models.Model):
    us = models.CharField(max_length=255)
