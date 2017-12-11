from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views
from django.views.generic.base import TemplateView

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('allauth.urls')),
	url(r'^accounts/profile/$', views.main.profile),

	url(r'^privateStuff/$', views.main.privateStuff),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]