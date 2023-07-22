# Register your models here.
from django.contrib import admin
from .models import User, Place

# Register your models with the admin site
admin.site.register(User)
admin.site.register(Place)
