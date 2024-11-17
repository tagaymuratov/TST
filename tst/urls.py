from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('tstapp.urls')),
    path('kzauth/', include('kzauth.urls', namespace='kzauth')),
    path('kzcart/', include('kzcart.urls', namespace='kzcart')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('tstapp/imgs/favicon.ico'))),
    path('favicon.svg', RedirectView.as_view(url=staticfiles_storage.url('tstapp/imgs/favicon.svg')))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "developed by Kezign"
admin.site.site_title = 'Администратирование сайта'