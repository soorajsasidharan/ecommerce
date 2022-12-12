from django.urls import reverse
import decimal
from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from turtle import update
from unicodedata import category
from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)


    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('store:category_list',args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/')
    slug = models.SlugField(max_length=255)
    price = models.FloatField(max_length=4)
    in_stock = models.BooleanField(default=True)
    is_activate = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail',args=[self.slug])

    def __str__(self):
        return self.title