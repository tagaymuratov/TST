from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tstapp.models import Product
from .cart import KzCart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
  cart = KzCart(request)
  product = get_object_or_404(Product, id=product_id)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product=product, quantity=cd['quantity'], overrideQuantity=cd['override'])
  return redirect('kzCart:cart_detail')


@require_POST
def cart_remove(request, product_id):
  cart = KzCart(request)
  product = get_object_or_404(Product, id=product_id)
  cart.remove(product)
  return redirect('kzCart:cart_detail')

def cart_detail(request):
  cart = KzCart(request)
  return render(request, 'kzCart/detail.html', {'cart':cart})
