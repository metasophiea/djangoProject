import django
from django.shortcuts import render

def guide(request, index=0):
	print("Guide page hit from user: " + str(request.user))

	template = django.template.loader.get_template('conVerse/guide.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))