from django.contrib import admin
from .models import *
# Register your models here.
class DetailsAdmin(admin.ModelAdmin):
    list_display=['Name','FirstName','Email','PhoneNumber']
admin.site.register(Details,DetailsAdmin)