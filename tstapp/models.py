from io import BytesIO
import os
from django.db import models
from django.urls import reverse
from django.core.files.base import ContentFile
from PIL import Image
from colorfield.fields import ColorField

class Product(models.Model):
  article = models.SlugField(max_length=32, unique=True, db_index=True, verbose_name='Артикль')
  title = models.CharField(max_length=128, verbose_name='Название')
  brand = models.ForeignKey('Brands', on_delete=models.DO_NOTHING, verbose_name='Бренд')
  description = models.TextField(blank=True, verbose_name='Описание')
  category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING, verbose_name='Категорея')
  subCat = models.ForeignKey('SubCats', on_delete=models.DO_NOTHING, verbose_name='Подкатегорея', blank=True, null=True)
  price = models.IntegerField(verbose_name='Цена')
  available = models.BooleanField(verbose_name='Товар в наличии', default=True)
  #sizes

  def __str__(self):
     return self.article
  class Meta:
      verbose_name='Товар'
      verbose_name_plural='Товары'
  def get_absolute_url(self):
      return reverse("product", kwargs={"product_slug": self.article})
  def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
  
class Images(models.Model): 
  article = models.ForeignKey('Product', on_delete=models.DO_NOTHING, verbose_name='Артикль')
  src = models.ImageField(upload_to='imgs/products/', verbose_name='Изображение')
  thumb = models.ImageField(upload_to='imgs/products/', verbose_name='Миниатюра', blank=True, editable=False)
  color = ColorField(blank=True)

  def __str__(self):
      return self.src.name
  class Meta:
      verbose_name='Изображение'
      verbose_name_plural='Изображения'

  def save(self, *args, **kwargs):
      img = Image.open(self.src)
      name, ext = os.path.splitext(self.src.name)
      img.thumbnail((700,700))
      temp_img = BytesIO()
      img.save(temp_img, format='webp', lossless=True, icc_profile=img.info.get('icc_profile'))
      temp_img.seek(0)
      self.thumb.save(name=name + '_mini.webp',content=ContentFile(temp_img.read()),save=False)
      temp_img.close()
      super().save(*args, **kwargs)

class Brands(models.Model):
  name = models.CharField(max_length=32, verbose_name='Бренд', unique=True)
  img = models.ImageField(upload_to='imgs/brands/', verbose_name='Лого', blank=True,)
  def __str__(self):
      return self.name
  class Meta:
      verbose_name='Бренд'
      verbose_name_plural='Бренды'
  
class Categories(models.Model):
  name = models.CharField(max_length=64, verbose_name='Категория', unique=True)
  img = models.ImageField(upload_to='imgs/cats/', verbose_name='Лого', blank=True,)
  def __str__(self):
      return self.name
  class Meta:
      verbose_name='Категория'
      verbose_name_plural='Категории'

class SubCats(models.Model):
    name = models.CharField(max_length=64, verbose_name='Подкатегория', unique=True)
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING, verbose_name='Категорея')
    def __str__(self):
      return self.name
    class Meta:
      verbose_name='Подкатегория'
      verbose_name_plural='Подкатегории'