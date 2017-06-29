# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import HumanResource
from HumanResource.models import user

# Create your models here.


class customer(user):
    website = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    trade_register = models.CharField(max_length=250)
    tax_id = models.CharField(max_length=250)
    RIB = models.CharField(max_length=250)
    if_entreprise= models.BooleanField(default=True)
    entreprise_type =  models.CharField(max_length=250)


    def __str__(self):
        return self.name_user + '  -  ' + self.email

class piste(models.Model):
    piste_objective = models.CharField(max_length=250)
    piste_staut = models.CharField(max_length=250)
    piste_categoty = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    client = models.ForeignKey(customer)

    def __str__(self):
        return self.piste_objective + '  -  ' + self.client + '  -  ' + self.description

class opportunity(models.Model):
    statut= models.CharField(max_length=250)
    next_action = models.CharField(max_length=250)
    ending_date =  models.DateTimeField
    priority = models.CharField(max_length=250)
    category= models.CharField(max_length=250)
    estimated_revenue = models.FloatField()
    client = models.ForeignKey(customer)
    def __str__(self):
        return self.client+ '  -  ' + self.statut + '  -  ' + self.priority




class category(models.Model):
    name_category = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name_category + '  -  ' + self.description



class ready_product(models.Model):
    name_product = models.CharField(max_length=250)
    category = models.ForeignKey(category)
    def __str__(self):
        return self.name_product + '  -  ' + self.category