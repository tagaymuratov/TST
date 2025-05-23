from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from tstapp.models import Brands, Product, Categories, Images, SubCats

def getProductList(income):
  pk_list = []
  obj = []
  for p in income:
    pk_list.append(p.pk)

  tempImgs = Images.objects.filter(article__in=pk_list)
  article = ' '
  
  for i in tempImgs:
    if article != i.article:
      article = i.article
      for p in income:
        if p == i.article:
          obj.append({
            'i' : i,
            'p' : p
          })
  
  return obj

def index(request):
  products = getProductList(Product.objects.all().order_by('-id')[:16])
  popular = getProductList(Product.objects.filter(popular = True)) 

  data = {
    'products' : products,
    'popular' : popular
  }

  return render(request, 'tstapp/index.html', context=data)

def product(request, product_slug):
  post = get_object_or_404(Product, article=product_slug)
  imgs = Images.objects.filter(article = post)

  colors_list = []
  colors_dict = {}
  for i in imgs:
    if i.color not in colors_list:
      colors_list.append(i.color)
  
  for c in colors_list:
    temp = []
    for i in imgs:
      if c == i.color:
        temp.append(i)
    colors_dict[c] = temp

  sames = getProductList(Product.objects.filter(category = post.category).exclude(id = post.pk).order_by('-id')[:8])
  fromBrand = getProductList(Product.objects.filter(brand = post.brand).exclude(id = post.pk).order_by('-id')[:8])

  data = {
    'p' : post,
    'i' : imgs,
    'sames' : sames,
    'brands': fromBrand,
    'colors':colors_dict
  }
  return render(request, 'tstapp/product.html', context=data)

def howto(request):
  return render(request, 'tstapp/howto.html')

def categories(request, id, subId=0):
  page = request.GET.get('page', 1)
  cats = Categories.objects.all().order_by('name')
  cat = cats.get(id=id)
  subCats = SubCats.objects.filter(category = cat).order_by('name')

  if subId != 0:
    subCat = subCats.get(id=subId)
    products = Product.objects.filter(subCat = subCat).order_by('-id')
  else:
    subCat = 0
    products = Product.objects.filter(category=cat).order_by('-id')
  
  product_list = []
  paginator = Paginator(products, 16)
  currentPage = paginator.page(int(page))
  for p in currentPage:
    product_list.append(p.pk)
  tempImgs = Images.objects.filter(article__in=product_list)
  cards = []
  article = ' '
  for i in tempImgs:
    if article != i.article: 
      article = i.article
      for p in products:
        if p == i.article:
          cards.append({ 'i':i, 'p':p })

  data = {
    'subCat': subCat,
    'subCats': subCats,
    'paginator':currentPage,
    'cats':cats,
    'cat':cat,
    'pi' : cards
  }
  return render(request, 'tstapp/categories.html', data)

def brands(request, id):
  page = request.GET.get('page', 1)
  brands = Brands.objects.all().order_by('name')
  brand = brands.get(id=id)
  products = Product.objects.filter(brand=brand).order_by('-id')
  product_pks = []
  paginator = Paginator(products, 16)
  currentPage = paginator.page(int(page))
  for p in currentPage:
    product_pks.append(p.pk)
  tempImgs = Images.objects.filter(article__in=product_pks)
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
    'paginator':currentPage,
    'brands':brands,
    'brand':brand,
    'pi':cards
  }
  return render(request, 'tstapp/brands.html', data)

def allcats(request):
  cats = Categories.objects.all().order_by('name')
  products = Product.objects.all().order_by('-id')[:16]
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
    'cats':cats,
    'items':prod
  }
  return render(request, 'tstapp/allcats.html', data)

def allBrands(request):
  brands = Brands.objects.all().order_by('name')
  products = getProductList(Product.objects.all().order_by('-id')[:16])

  data = {
    'brands':brands,
    'items' : products
  }
  return render(request, 'tstapp/allbrands.html', data)

def contacts(request):
  return render(request, 'tstapp/contacts.html')

def about(request):
  return render(request, 'tstapp/about.html')

def search(request):
  q = request.GET.get('q')
  page = request.GET.get('page', 1)
  products = Product.objects.filter(title__icontains=q) | Product.objects.filter(description__icontains=q) | Product.objects.filter(article__icontains=q)
  paginator = Paginator(products, 16)
  currentPage = paginator.page(int(page))
  product_pks = []
  for p in currentPage:
    product_pks.append(p.pk)
  tempImgs = Images.objects.filter(article__in=product_pks)
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

  data={
    'q':q,
    'paginator':currentPage,
    'pi':cards
  }
  return render(request, 'tstapp/search.html', data)

def certs(request):
  return render(request, 'tstapp/certs.html')