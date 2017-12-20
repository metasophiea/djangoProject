from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
import allauth.account.views

from conVerse import views

urlpatterns = [
	# Main adin address
	url(r'^admin/', admin.site.urls),


	# Authentication addresses
	url(r'^account/', include('allauth.urls')), # still needed to cover provider login
		#
	url(r'^signup/', allauth.account.views.signup, name='account_signup'), #signup.html
	url(r'^login/', allauth.account.views.login, name='account_login'), # login.html
	url(r'^logout/', allauth.account.views.logout, name='account_logout'), # logout.html
	url(r"^inactive/$", allauth.account.views.account_inactive, name="account_inactive"), # inactive.html
	url(r'^setPassword/', allauth.account.views.password_set, name='account_set_password'), # password_set.html
	url(r'^changePassword/', allauth.account.views.password_change, name='account_change_password'), # password_change.html
	url(r"^resetPassword/key/done/$", allauth.account.views.password_reset_from_key_done, name="account_reset_password_from_key_done"), # password_reset_from_key_done.html
	url(r"^resetPassword/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", allauth.account.views.password_reset_from_key, name="account_reset_password_from_key"), # password_reset_from_key.html
	url(r"^resetPassword/done/$", allauth.account.views.password_reset_done, name="account_reset_password_done"), # password_reset_done.html
    url(r'^resetPassword/', allauth.account.views.password_reset, name='account_reset_password'), # password_reset.html
	url(r"^confirmEmail/(?P<key>[-:\w]+)/$", allauth.account.views.confirm_email, name="account_confirm_email"), # email_confirm.html
	url(r"^confirmEmail/$", allauth.account.views.email_verification_sent, name="account_email_verification_sent"), # verification_sent.html
    url(r'^manageEmail/', allauth.account.views.email, name='account_email'), # email.html


	# Other addresses
	url(r'^verseData/(?P<start>(\d+))/(?P<end>(\d+))/$', views.api_getVerse.getVerse),
	url(r'^verseData/(?P<index>(\d+))/$', views.api_getVerse.getVerse),
	url(r'^verseData/$', views.api_getVerse.getVerse, name='api_verseData'),

	url(r'^profile/', views.profile.profile),
	url(r'^verse/', views.verse.verse),

	# Landing page
	url(r'^$', views.index.index)
]