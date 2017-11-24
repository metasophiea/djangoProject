from django.contrib import admin
from .models import *

class tweet_admin(admin.ModelAdmin):
	list_display = ['tweetId','author','text','upVotes','downVotes']

admin.site.register(tweet, tweet_admi