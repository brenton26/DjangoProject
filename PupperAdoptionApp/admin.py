from django.contrib import admin
from .models import Dog, TempDog

# Register your models here.
admin.site.register(TempDog)
admin.site.register(Dog)