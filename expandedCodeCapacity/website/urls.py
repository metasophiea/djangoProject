from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^login/', views.auth.login),
	url(r'^logout/', views.auth.logout),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]