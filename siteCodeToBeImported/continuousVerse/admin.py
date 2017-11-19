import django
from .models import *

class verse_admin(django.contrib.admin.ModelAdmin):
    list_display = ["verseId","position","author","upvotes","downvotes"]
    ordering = ['position']

django.contrib.admin.site.register(verse, verse_admin)