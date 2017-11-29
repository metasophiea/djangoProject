from django.contrib import admin
from . import models

class tweet_admin(admin.ModelAdmin):
	list_display = ['tweetId','author','text','upVotes','downVotes']

admin.site.register(models.tweet.tweet, tweet_admin)