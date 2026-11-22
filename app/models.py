from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    email = models.CharField(max_length=100)

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    PRODUCTS = [ ('smartphone','smartphone'),('notebook','notebook'),('smartTV','smartTV')   ]
    product = models.CharField(choices=PRODUCTS,max_length=10,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    voltage = models.CharField(max_length=100,null=False,blank=False)
    dimension = models.CharField(max_length=100,null=False,blank=False)
    screen_resolutions = models.CharField(max_length=100,null=False,blank=False)
    storage_capacity = models.CharField(max_length=100,null=False,blank=False)
    connectivity = models.JSONField(default=list)  
    stock = models.PositiveIntegerField(blank=False,null=False)
    min_stock = models.PositiveIntegerField(blank=False,null=False)  

class Movimentation(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    TYPE= [('input','input'),('output','output')]
    type = models.CharField(choices=TYPE,null=False,blank=False,max_length=10)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    quantity = models.PositiveIntegerField(blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)


    


