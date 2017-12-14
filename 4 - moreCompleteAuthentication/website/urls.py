from django.conf.urls import url, include
from django.contrib import admin
from newTwitter import views
from django.views.generic.base import TemplateView
import allauth.account.views
import django

import newCode

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	
	url(r'^signup/$', allauth.account.views.SignupView.as_view(), name='account_signup'),
	url(r'^login/$', allauth.account.views.LoginView.as_view(), name='account_login'),
	url(r'^logout/$', allauth.account.views.LogoutView.as_view(), name='account_logout'),
	# (no 'as_view' - *name)
	# AccountInactiveView				AddEmailForm					AjaxCapableProcessFormViewMixin
	# ChangePasswordForm				CloseableSignupMixin			ConfirmEmailView
	# EmailAddress						EmailConfirmation				EmailConfirmationHMAC
	# EmailVerificationSentView			EmailView						FormView
	# Http404							HttpResponsePermanentRedirect	HttpResponseRedirect
	# INTERNAL_RESET_SESSION_KEY		INTERNAL_RESET_URL_KEY			ImmediateHttpResponse
	# LoginForm							LoginView						LogoutView
	# PasswordChangeView				PasswordResetDoneView			PasswordResetFromKeyDoneView
	# PasswordResetFromKeyView			PasswordResetView				PasswordSetView
	# RedirectAuthenticatedUserMixin	ResetPasswordForm				ResetPasswordKeyForm
	# SetPasswordForm				   *SignupForm						SignupView
	# TemplateResponseMixin				TemplateView					UserTokenForm
	# View

	url(r'^account/', include('allauth.urls')),
	# /signup
	# /login
	# /logout
	# /password/set
	# /password/change
	# /inactive
	# /email
	# /confirm-email
	# /password/reset/
	# /password/reset/done/
	# /password/reset/key/
	# /password/reset/key/done

	url(r'^privateStuff/$', views.main.privateStuff),
	url(r'^otherPrivateStuff/$', views.main.otherPrivateStuff),

	url(r'^newCode/', include('newCode.urls')),

	url(r'^tweetData/', views.data.getTweets),
	url(r'^$', views.main.index)
]