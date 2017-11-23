import django
from django.db import models

class verse(django.db.models.Model):
    verseId = django.db.models.AutoField(primary_key=True)

    author = django.db.models.CharField(max_length=100)
    authorId = models.ForeignKey(django.conf.settings.AUTH_USER_MODEL)

    text = django.db.models.CharField(max_length=1024)

    position = django.db.models.IntegerField(default=0)
    upvotes = django.db.models.IntegerField(default=0)
    downvotes = django.db.models.IntegerField(default=0)

    def __str__(self):
        return "verse: " + str(self.verseId) + " in position: " + str(self.position) + " written by: " + self.author