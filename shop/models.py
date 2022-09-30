from distutils.command.upload import upload
from time import timezone
from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50 , unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta():
        ordering = ['position']
    def __str__(self):
        return self.title

class Cp(models.Model):
    VASIYAT = (
        ('موجود' , 'Mojood'),
        ('ناموجود' , 'NaMojood'),
        ('به زودی...' , 'BaZoodi'),
    )
    onvan = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50 , unique=True)
    tozihat = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='img/')
    price = models.CharField(max_length=30)
    category = models.ManyToManyField(Category , related_name='Cp')
    zaman = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50 , choices=VASIYAT)

    def __str__(self):
        return self.onvan