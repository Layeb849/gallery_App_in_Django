"""
URL configuration for newProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newApp.views import album_list, album_detail, upload_photo,home, delete_image, edit_album,delete_album
from newProject import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'), 
    path('album_list/', album_list, name='album_list'),
    path('album/<int:album_id>/', album_detail, name='album_detail'),
    path('album/<int:album_id>/upload/', upload_photo, name='upload_photo'),
    path('delete_image/<int:photo_id>/', delete_image, name='delete_image'),    
    path('edit_album/<int:album_id>/', edit_album, name='edit_album'),
     path('delete_album/<int:album_id>/', delete_album, name='delete_album'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
