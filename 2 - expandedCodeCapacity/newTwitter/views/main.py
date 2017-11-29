import django
from django.shortcuts import render

def index(request):
	print("Main page hit from user: " + str(request.user))

	template = django.template.loader.get_template('newTwitter/index.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))