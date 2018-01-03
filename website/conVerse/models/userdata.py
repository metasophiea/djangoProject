from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

class userdata(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    screenname = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return str(self.username) + " - " + str(self.screenname)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_userdata(sender, instance, created, **kwargs):
        if created:
            userdata.objects.create(username=instance)
            instance.userdata.screenname = instance.userdata.username.username
            instance.userdata.save()

from django.contrib import admin
class userdata_admin(admin.ModelAdmin):
    list_display = ['username','screenname']
admin.site.register(userdata, userdata_admin)