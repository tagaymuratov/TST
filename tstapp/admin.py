from django.contrib import admin
from django.utils.html import format_html
from .models import Brands, Categories, Images, Product, SubCats

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  ordering = ['article']
  list_display = ('article', 'category', 'subCat', 'brand', 'available',)
  list_display_links = ('article',)
  list_per_page = 20
  search_fields = ['article']
  list_filter = ['category__name', 'subCat__name', 'brand__name', 'available']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  ordering = ['name']
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
  list_per_page = 20
  def image_tag(self, obj):
    return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.thumb.url))
  
  image_tag.short_description = 'Image'
  list_display = ['image_tag','src', ]

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
  ordering = ['name']

@admin.register(SubCats)
class SubCatsAdmin(admin.ModelAdmin):
  ordering = ['name']
  list_display = ['name', 'category']