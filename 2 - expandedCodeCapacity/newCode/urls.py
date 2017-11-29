from django.conf.urls import url, include

from . import data, info

urlpatterns = [
	url(r'^codeLib/', include('newCode.codeLib.urls')),
	url(r'^info/', info.index),
    url(r'^$', data.index),
]