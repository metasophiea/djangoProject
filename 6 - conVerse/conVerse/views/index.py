import django
from django.shortcuts import render

def index(request, index=0):
	print("Main page hit from user: " + str(request.user))

	template = django.template.loader.get_template('conVerse/index.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))