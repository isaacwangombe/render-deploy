from django.shortcuts import render
from django.http  import HttpResponse
from .models import GalleryCategories, GalleryImages, GalleryLocations

# Create your views here.

def gallery(request):
    images = GalleryImages.get_all()
    location = GalleryLocations.get_all(id)

    return render(request, 'photos/photos.html', {'images': images, 'location':location})




def category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images = GalleryImages.search_image(search_term)

        message = f'{search_term}'

        return render(request, 'photos/category.html', {'message':message, 'images':images})
    else:
        message = 'You have not searched any term'
        return render(request, 'photos/category.html', {'message':message})

def location(request):
        search_term = request.GET.get('location')
        images = GalleryImages.filter_by_location(search_term)
        message = f'{search_term}'
        location = GalleryLocations.get_all(id)

        return render(request, 'photos/location.html', {'message':message, 'images':images,'location':location})
   