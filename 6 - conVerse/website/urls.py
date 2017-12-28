from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
import allauth.account.views

from auth import views as extraAuthViews
from conVerse import views

handler400 = 'conVerse.views.pageError.handler400' # bad request
handler403 = 'conVerse.views.pageError.handler403' # permission denied
handler404 = 'conVerse.views.pageError.handler404' # page not found
handler500 = 'conVerse.views.pageError.handler500' # internal server error

urlpatterns = [
	# Main admin address
	url(r'^admin/', admin.site.urls),


	# Authentication addresses
	url(r'^account/', include('allauth.urls')), # still needed to cover provider login
		#
	url(r'^signup/', allauth.account.views.signup, name='account_signup'), 																						# auth/templates/auth/account/signup.html
	url(r'^login/', allauth.account.views.login, name='account_login'), 																						# auth/templates/auth/account/login.html
	url(r'^logout/', allauth.account.views.logout, name='account_logout'), 																						# auth/templates/auth/account/logout.html
	url(r"^inactive/$", allauth.account.views.account_inactive, name="account_inactive"), 																		# auth/templates/auth/account/inactive.html
	url(r'^setPassword/', allauth.account.views.password_set, name='account_set_password'), 																	# auth/templates/auth/account/password_set.html
	url(r'^changePassword/', allauth.account.views.password_change, name='account_change_password'), 															# auth/templates/auth/account/password_change.html
	url(r"^resetPassword/key/done/$", allauth.account.views.password_reset_from_key_done, name="account_reset_password_from_key_done"), 						# auth/templates/auth/account/password_reset_from_key_done.html
	url(r"^resetPassword/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", allauth.account.views.password_reset_from_key, name="account_reset_password_from_key"), 	# auth/templates/auth/account/password_reset_from_key.html
	url(r"^resetPassword/done/$", allauth.account.views.password_reset_done, name="account_reset_password_done"), 												# auth/templates/auth/account/password_reset_done.html
    url(r'^resetPassword/', allauth.account.views.password_reset, name='account_reset_password'), 																# auth/templates/auth/account/password_reset.html
	url(r"^confirmEmail/(?P<key>[-:\w]+)/$", allauth.account.views.confirm_email, name="account_confirm_email"), 												# auth/templates/auth/account/email_confirm.html
	url(r"^confirmEmail/$", allauth.account.views.email_verification_sent, name="account_email_verification_sent"), 											# auth/templates/auth/account/verification_sent.html
    url(r'^manageEmail/', allauth.account.views.email, name='account_email'), 																					# auth/templates/auth/account/email.html
    url(r'^deleteAccount/$', extraAuthViews.deleteAccount.deleteAccount, name='account_delete'), 																# auth/templates/auth/account/account_delete.html (this is an addition)
    url(r'^socialSignup/$', allauth.socialaccount.views.signup, name='socialaccount_signup'), 																	# auth/templates/auth/socialaccount/signup.html (used when the third-party sign-in uses an email address that's already in use)
	url(r'^socialConnections/$', allauth.socialaccount.views.connections , name='socialaccount_connections'), 													# auth/templates/auth/socialaccount/connections.html


	# Other addresses
	url(r'^verseData/(?P<start>(\d+))/(?P<end>(\d+))/$', views.api_getVerse.api_getVerse),
	url(r'^verseData/(?P<index>(\d+))/$', views.api_getVerse.api_getVerse),
	url(r'^verseData/$', views.api_getVerse.api_getVerse, name='api_verseData'),

	url(r'^updateScreenname/$', views.api_updateUserdata.api_updateScreenname, name='api_updateScreenname'),
	url(r'^updateVersePosition/$', views.api_updateVerse.api_updatePosition, name='api_updateVersePosition'),
	url(r'^updateVerse/$', views.api_updateVerse.api_updateVerse, name='api_updateVerse'),

	url(r'^profile/$', views.profile.profile, name='profile'),
	url(r'^verse/(?P<index>(\d+))/$', views.verse.verse),


	# Landing page
	url(r'^(?P<index>(\d+))/$', views.index.index),
	url(r'^$', views.index.index)
]