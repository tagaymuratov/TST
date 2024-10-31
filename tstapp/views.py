from django.shortcuts import get_object_or_404, render
from django.db.models import F
from tstapp.models import Brands, Product, Categories, Images

def index(request):
  products = Product.objects.all().order_by('-id')[:8]
  products_list = []
  for p in products:
    products_list.append(p.pk)

  tempImgs = Images.objects.filter(article__in=products_list)
  prod = []
  article = ' '

  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in products:
        if p == i.article:
          prod.append({
            'i' : i,
            'p' : p
          })

  data = {
    'products' : prod,
  }

  return render(request, 'tstapp/index.html', context=data)

def product(request, product_slug):
  post = get_object_or_404(Product, article=product_slug)
  imgs = Images.objects.filter(article = post)

  same = Product.objects.filter(category = post.category).exclude(id = post.pk)[:5]
  same_list = []
  for s in same:
    same_list.append(s.pk)
  tempImgs = Images.objects.filter(article__in=same_list)
  sames = []
  article = ' '
  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in same:
        if p == i.article:
          sames.append({
            'i' : i,
            'p' : p
          })

  brand_prod = Product.objects.filter(brand = post.brand).exclude(id = post.pk)[:5]
  brand_list = []
  for b in brand_prod:
    brand_list.append(b.pk)
  tempImgs = Images.objects.filter(article__in=brand_list)
  fromBrand = []
  article = ' '
  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in brand_prod:
        if p == i.article:
          fromBrand.append({
            'i' : i,
            'p' : p
          })

  data = {
    'p' : post,
    'i' : imgs,
    'sames' : sames,
    'brands': fromBrand,
    'brandTitle': post.brand.name
  }
  return render(request, 'tstapp/product.html', context=data)

def howto(request):
  return render(request, 'tstapp/howto.html')

def categories(request, id):
  cat = Categories.objects.get(id=id)
  products = Product.objects.filter(category=cat)
  product_list = []
  for p in products:
    product_list.append(p.pk)
  tempImgs = Images.objects.filter(article__in=product_list)
  cards = []
  article = ' '
  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in products:
        if p == i.article:
          cards.append({
            'i' : i,
            'p' : p
          })

  data = {
    'title':cat,
    'pi' : cards
  }
  return render(request, 'tstapp/categories.html', data)

def brands(request, id):
  brand = Brands.objects.get(id=id)
  products = Product.objects.filter(brand=brand)
  product_list = []
  for p in products:
    product_list.append(p.pk)
    tempImgs = Images.objects.filter(article__in=product_list)
  cards = []
  article = ' '
  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in products:
        if p == i.article:
          cards.append({
            'i' : i,
            'p' : p
          })

  data = {
    'title':brand.name,
    'pi':cards
  }
  return render(request, 'tstapp/brands.html', data)

def allcats(request):
  cats = Categories.objects.all()
  data = {
    'cats':cats
  }
  return render(request, 'tstapp/allcats.html', data)

def allBrands(request):
  brands = Brands.objects.all()
  data = {
    'brands':brands
  }
  return render(request, 'tstapp/allbrands.html', data)

def contacts(request):
  return render(request, 'tstapp/contacts.html')