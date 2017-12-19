from django.db import models
from django.conf import settings

class userdata(models.Model):
    allauthUser = models.ForeignKey(settings.AUTH_USER_MODEL)
    screenName = models.CharField(max_length=100)

    def __str__(self):
        return "User: " + str(self.allauthUser) + " with screenname " + str(self.screenName)

from django.contrib import admin
class userdata_admin(admin.ModelAdmin):
    list_display = ['allauthUser','screenName']
admin.site.register(userdata, userdata_admin)