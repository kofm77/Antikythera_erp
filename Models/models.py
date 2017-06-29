# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

import HumanResource
import sales
from HumanResource.models import user

from sales.models import customer

class bill(models.Model):
    id_bill = models.CharField(primary_key=True, max_length=50)
    client_name= models.ForeignKey(sales.customer)
    Date = models.DateTimeField
    def __str__(self):
        return self.name_user + '  -  ' + self.email

class quotation(models.Model):
    id_quotation = models.CharField(primary_key=True, max_length=50)
    client_name= models.ForeignKey(customer)
    Date = models.DateTimeField
    def __str__(self):
        return self.name_user + '  -  ' + self.email

class claim(models.Model):
    claimer = models.ForeignKey(HumanResource.user)
    subject = models.CharField(max_length=250)
    claim_body = models.CharField(max_length=5000)
    priority = models.CharField(max_length=250)
    deadline = models.DateTimeField
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.claim_body