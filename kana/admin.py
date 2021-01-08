from django.contrib import admin
from .models import Kana, Sound, Type

# Register your models here.

admin.site.register(Kana)
admin.site.register(Sound)
admin.site.register(Type)