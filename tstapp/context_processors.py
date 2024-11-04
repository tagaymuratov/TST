
from tstapp.models import Categories, Brands


def db_categories(request):
  cats = Categories.objects.all().order_by('name')
  return {'db_cats':cats}

def db_brands(request):
  brands = Brands.objects.all().order_by('name')
  return {'db_brands':brands}
