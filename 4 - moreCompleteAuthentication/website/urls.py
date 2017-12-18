from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views
from django.views.generic.base import TemplateView
import allauth.account.views
import django

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),


	# Authentication addresses
	# url(r'^account/', include('allauth.urls')),
	url(r'^signup/', allauth.account.views.signup, name='account_signup'),
	url(r'^login/', allauth.account.views.login, name='account_login'),
	url(r'^logout/', allauth.account.views.logout, name='account_logout'),
	url(r"^inactive/$", allauth.account.views.account_inactive, name="account_inactive"),
	url(r'^setPassword/', allauth.account.views.password_set, name='account_set_password'),
	url(r'^changePassword/', allauth.account.views.password_change, name='account_change_password'),
    url(r'^resetPassword/', allauth.account.views.password_reset, name='account_reset_password'),
	url(r"^resetPassword/done/$", allauth.account.views.password_reset_done, name="account_reset_password_done"),
    url(r"^resetPassword/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", allauth.account.views.password_reset_from_key, name="account_reset_password_from_key"),
    url(r"^resetPassword/key/done/$", allauth.account.views.password_reset_from_key_done, name="account_reset_password_from_key_done"),
	url(r"^confirmEmail/$", allauth.account.views.email_verification_sent, name="account_email_verification_sent"),
    url(r"^confirmEmail/(?P<key>[-:\w]+)/$", allauth.account.views.confirm_email, name="account_confirm_email"),
	url(r'^manageEmail/', allauth.account.views.email, name='account_email'),


	url(r'^privateStuff/$', views.main.privateStuff),
	url(r'^otherPrivateStuff/$', views.main.otherPrivateStuff),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]