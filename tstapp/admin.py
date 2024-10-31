from django.contrib import admin
from django.utils.html import format_html
from .models import Brands, Categories, Images, Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('article', 'category', 'brand', 'available',)
  list_display_links = ('article',)
  list_per_page = 10
  search_fields = ['article']
  list_filter = ['category__name', 'brand__name', 'available']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
  list_per_page = 10
  def image_tag(self, obj):
    return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.thumb.url))
  
  image_tag.short_description = 'Image'
  list_display = ['image_tag','src', ]


admin.site.register(Brands)