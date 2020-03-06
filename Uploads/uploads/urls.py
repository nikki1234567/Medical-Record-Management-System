from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
   
    path('upload/',views.uploads,name="Upload"),
    path('files/',views.temporary_files,name="Files")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)