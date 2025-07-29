from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('categories/<int:id>/<int:subId>/', views.categories, name='categories'),
    path('categories/<int:id>/', views.categories, name='categories'),
    path('brands/<int:id>/', views.brands, name='brands'),
    path('allcats/', views.allcats, name='allcats'),
    path('allbrands/', views.allBrands, name='allbrands'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('certs/', views.certs, name='certs'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('article/<int:id>/', views.article, name='article'),
    path('sg360-1/', views.sg360_1, name='sg360-1'),
    path('sg360-2/', views.sg360_2, name='sg360-2')
]