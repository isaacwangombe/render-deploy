from django.contrib import admin
from .models import GalleryImages, GalleryCategories, GalleryLocations

# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(GalleryImages, ImagesAdmin)
admin.site.register(GalleryCategories)
admin.site.register(GalleryLocations)