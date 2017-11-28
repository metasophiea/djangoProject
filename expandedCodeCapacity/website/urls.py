from django.conf.urls import url
from django.contrib import admin
from newTwitter import views

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^login/', views.auth.login),
	url(r'^logout/', views.auth.logout),

	url(r'^data/', newCode.data.index),
	url(r'^info/', newCode.info.index),
	url(r'^codeLib/', newCode.codeLib.func.index),

	url(r'^moreData/', views.data.index),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]