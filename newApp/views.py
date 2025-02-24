from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from .forms import PhotoUploadForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, "gallery/album_list.html", {"albums": albums})


def album_list(request):
    albums = Album.objects.all() 

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name:  
            Album.objects.create(name=name, description=description)
            return redirect("album_list") 

    return render(request, "album_list.html", {"albums": albums})


def home(request):
    return render(request, "home.html")


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, "gallery/album_detail.html", {"album": album})

def upload_photo(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album
            photo.save()
            return redirect("album_detail", album_id=album.id)
    else:
        form = PhotoUploadForm()

    return render(request, "gallery/upload_photo.html", {"form": form, "album": album})


def delete_image(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user == photo.album.user: 
        photo.delete()  
        return redirect('home') 
    else:
        return redirect('home') 