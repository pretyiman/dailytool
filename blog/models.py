from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import models,transaction
from django.urls import reverse
from django.utils.text import slugify
import string
import random

class rack(models.Model):
    Rack = models.CharField(null=True,max_length=100)

    def save(self, *args, **kwargs):
        self.Rack = self.Rack.upper()
        super(rack, self).save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('rack-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.Rack)

class warehouse(models.Model):
    Name = models.CharField(null=True,max_length=100)

    def save(self, *args, **kwargs):
        self.Name = self.Name.upper()
        super(warehouse, self).save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('warehouse-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.Name)

class catagory(models.Model):
    Name = models.CharField(max_length=100,unique=True,null=True)

    def save(self, *args, **kwargs):
        self.Name = self.Name.upper()
        super(catagory, self).save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('catagory-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.Name)

class subcatagory(models.Model):
    Name = models.CharField(max_length=100,unique=True,null=True)

    def save(self, *args, **kwargs):
        self.Name = self.Name.upper()
        super(subcatagory, self).save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('subcatagory-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.Name)


class Expenses(models.Model):
    reg_date = models.DateField(auto_now_add=True)
    exp_id = models.AutoField(primary_key=True)  # F
    description = models.CharField(max_length=200)
    expenses_value = models.IntegerField()


    def __str__(self):
        return str(self.exp_id)


class Income(models.Model):
    reg_date = models.DateField(auto_now_add=True)
    income_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    income_value = models.IntegerField()


    def __str__(self):
        return str(self.income_id)

class Contacts(models.Model):
    reg_date = models.DateField(auto_now_add=True)
    contact_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=17,null=False, blank=False, unique=True)
    Address = models.CharField(max_length=250, null=False)

    def __str__(self):
        return str(self.contact_ID)

    def save(self, force_insert=False, force_update=False):
        self.Name = self.Name.upper()
        super(Contacts, self).save(force_insert, force_update)

class list(models.Model):
    item = models.CharField(max_length=150)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

class item(models.Model):
    Barcode = models.CharField(max_length=16, null=True, unique=True)
    Name = models.CharField(max_length=100, null=True,unique=True)
    Catagory = models.ForeignKey(catagory,on_delete=models.SET_NULL,null=True)
    Sub_Catagory = models.ForeignKey(subcatagory,on_delete=models.SET_NULL, null=True)
    Sale_Price = models.CharField(max_length=100, null=True)
    Stock = models.CharField(max_length=100, null=True)
    Warehouse = models.ForeignKey(warehouse,on_delete=models.SET_NULL, null=True)
    Rack = models.ForeignKey(rack,on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.Name = self.Name.upper()
        super(item, self).save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('item-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.Name)
