from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views
from django.views.generic.base import TemplateView

import newCode

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
	url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),

	url(r'^admin/', admin.site.urls),

	url(r'^login/', views.auth.login),
	url(r'^logout/', views.auth.logout),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', TemplateView.as_view(template_name='index.html')),
	url(r'^$', views.main.index)
]