from django.db import models
from django.conf import settings

class verse(models.Model):
    allauthUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verseId = models.AutoField(primary_key=True)
    position = models.IntegerField(default=0)
    text = models.CharField(max_length=100, blank=True)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)

    def __str__(self):
        return "Verse number: " + str(self.allauthUser) + " with verseId " + str(self.verseId)

from django.contrib import admin
class verse_admin(admin.ModelAdmin):
    list_display = ['allauthUser','verseId','position','text']
admin.site.register(verse, verse_admin)