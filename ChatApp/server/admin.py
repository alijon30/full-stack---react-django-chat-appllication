from django.contrib import admin

# Register your models here.
from .models import Channel, Category, Server

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Server)

