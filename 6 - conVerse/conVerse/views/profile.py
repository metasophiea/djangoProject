import django
from .. import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	print("Profile page hit from user: " + str(request.user))

	userdataQuery = models.userdata.userdata.objects.get(username=request.user)
	try:    verse = models.verse.verse.objects.get(allauthUser=request.user).text
	except: verse = ""

	template = django.template.loader.get_template('conVerse/profile.html')
	context = {
		'userdata':userdataQuery,
		'verse':verse
	}
	return django.http.HttpResponse(template.render(context, request))