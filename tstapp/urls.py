from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('categories/<int:id>', views.categories, name='categories'),
    path('brands/<int:id>', views.brands, name='brands'),
    path('howto/', views.howto, name='howto'),
    path('allcats/', views.allcats, name='allcats'),
    path('allbrands/', views.allBrands, name='allbrands')
]