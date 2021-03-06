import django
from .. import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	print("Profile page hit from user: " + str(request.user))

	userdataQuery = models.userdata.userdata.objects.get(username=request.user)
	try:    verse = models.verse.verse.objects.get(allauthUser=request.user)
	except: verse = ""

	template = django.template.loader.get_template('conVerse/profile.html')
	context = {
		'userdata':userdataQuery,
		'verse':verse,
		'screennameMaxLength': models.userdata.userdata._meta.get_field('screenname').max_length,
		'verseMaxLength': models.verse.verse._meta.get_field('text').max_length
	}
	return django.http.HttpResponse(template.render(context, request))