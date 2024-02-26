from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject']
    
