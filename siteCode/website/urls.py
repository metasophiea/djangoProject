from django.conf.urls import url
from django.contrib import admin
from newTwitter import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^login/', views.login),
	url(r'^logout/', views.logout),

	url(r'^tweetData/', views.getTweets),
	url(r'^$', views.index)
]