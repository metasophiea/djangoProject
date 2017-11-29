from django.conf.urls import url

from . import func

urlpatterns = [
    url(r'^func/', func.index),
    url(r'^$', func.index)
]