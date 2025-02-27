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
    photo = Photo.objects.get(id=photo_id)
    photo.delete()  
    return redirect('album_list') 

def edit_album(request, album_id):
    albums = get_object_or_404(Album, id=album_id)  # This ensures the album exists

    if request.method == "POST":
        al_name = request.POST.get("name")
        al_description = request.POST.get("description")
        
        # Update album fields directly
        albums.name = al_name
        albums.description = al_description
        albums.save()
        return redirect("album_list")
        # return render(request, "edit_album.html", {'data': albums})

    # This line handles GET requests
    return render(request, "edit_album.html", {'data': albums})


def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return redirect('album_list')  