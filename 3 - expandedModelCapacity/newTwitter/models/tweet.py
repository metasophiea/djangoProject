from django.db import models
from django.conf import settings

class tweet(models.Model):
        tweetId = models.AutoField(primary_key=True)

        author = models.CharField(max_length=100)
        authorId = models.ForeignKey(settings.AUTH_USER_MODEL)

        text = models.CharField(max_length=140)

        upVotes = models.IntegerField(default=0)
        downVotes = models.IntegerField(default=0)

        def __str__(self):
                return "Tweet: " + str(self.tweetId) + " by " + str(self.author)








from django.contrib import admin

class tweet_admin(admin.ModelAdmin):
        list_display = ['tweetId','author','text','upVotes','downVotes']

admin.site.register(tweet, tweet_admin)
