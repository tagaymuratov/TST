
from tstapp.models import Categories, Brands


def db_categories(request):
  cats = Categories.objects.all()
  return {'db_cats':cats}

def db_brands(request):
  brands = Brands.objects.all()
  return {'db_brands':brands}
