from django.db import models
import os

# Create your models here.

def get_image_path(instance, filename):
    return 'img/'+filename

class Category(models.Model):
    category = models.CharField(max_length=50,verbose_name='Kategori', unique=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategori'

class New(models.Model):

    image = models.ImageField(upload_to=get_image_path, blank=True, null=True,verbose_name='Fotograf')
    name = models.TextField(verbose_name='Haberin Adı')
    content = models.TextField(verbose_name='Haberin İçeriği')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Kategori')
    date = models.DateTimeField(max_length=50,verbose_name='Tarih')
    editor = models.CharField(max_length=50,verbose_name='Haberi Yayınlayan')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haber'
    
    

