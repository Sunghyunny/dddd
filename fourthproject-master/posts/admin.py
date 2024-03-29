from django.contrib import admin
from .models import Models, Photo

# Register your models here.


class ModelAdmin(admin.ModelAdmin):
     list_filter = ('gender', 'category')


class PhotoAdmin(admin.ModelAdmin):
     list_filter = ('gender', 'category')

admin.site.register(Models, ModelAdmin)
admin.site.register(Photo, PhotoAdmin)