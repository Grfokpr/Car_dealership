from django.contrib import admin

# Register your models here.
from .models import Dealership, Car, Manufacturer
admin.site.register(Dealership)
admin.site.register(Car)
admin.site.register(Manufacturer)
