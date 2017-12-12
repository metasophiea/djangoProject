from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views
from django.views.generic.base import TemplateView
import allauth.account.views
import django

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^signup/$', lambda request: django.http.HttpResponseRedirect("/accounts/signup"), name='signup'),
	url(r'^login/$', lambda request: django.http.HttpResponseRedirect("/accounts/login"), name='login'),
	url(r'^logout/$', lambda request: django.http.HttpResponseRedirect("/accounts/logout"), name='logout'),

    url(r'^accounts/', include('allauth.urls')),
	# /signup
	# /login
	# /logout
	# /password/change
	# /password/set
	# /inactive
	# /email
	# /confirm-email
	# /password/reset/done/
	# /password/reset/key/done

	url(r'^privateStuff/$', views.main.privateStuff),
	url(r'^otherPrivateStuff/$', views.main.otherPrivateStuff),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]