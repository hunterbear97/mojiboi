from django.contrib import admin
from .models import Radical, Meaning, Kanji, Sound, Tag

# Register your models here.
admin.site.register(Radical)
admin.site.register(Meaning)
admin.site.register(Sound)
admin.site.register(Tag)
admin.site.register(Kanji)