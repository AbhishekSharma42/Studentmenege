from csv import list_dialects
from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class Author(admin.ModelAdmin):
    list_display=['id','stuName','stuMob','stuEmail','bran']

@admin.register(IntrestStu)
class Intrest(admin.ModelAdmin):
    list_display=['id','stuName','stuMob','stuEmail','bran']
