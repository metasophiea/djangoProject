import django
from django.shortcuts import render

def verse(request, index=0):
	print("Verse page " + index + " hit from user: " + str(request.user))

	template = django.template.loader.get_template('conVerse/verse.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))