# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    num_employee = models.CharField(max_length=250)
    department_manager = models.CharField(max_length=250)
    def __str__(self):
        return self.name + '  -  ' + self.description

class Employee(models.Model):
    role = models.CharField(max_length=250)

    salary = models.IntegerField
    department = models.ForeignKey(Department)
    def __str__(self):
        return self.name_user + '  -  ' + self.email+ '  -  ' + self.position