from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('tstapp.urls')),
    path('kzauth/', include('kzauth.urls', namespace='kzauth')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "developed by Kezign"
admin.site.site_title = 'Администратирование сайта'
