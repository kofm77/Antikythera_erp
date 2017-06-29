# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models



class user(models.Model):
    name_user = models.CharField(max_length=250)
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    city= models.CharField(max_length=250)
    country = models.CharField( max_length=250)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name_user + '  -  ' + self.email




class Department(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    num_employee = models.CharField(max_length=250)
    department_manager = models.CharField(max_length=250)
    def __str__(self):
        return self.name + '  -  ' + self.description

class Employee(user):
    role = models.CharField(max_length=250,default='')
    salary = models.IntegerField(default='')
    department = models.ForeignKey(Department)
    def __str__(self):
        return self.name_user + '  -  ' + self.email+ '  -  ' + self.position