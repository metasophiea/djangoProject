import django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
	print("Main page hit from user: " + str(request.user))

	template = django.template.loader.get_template('newTwitter/index.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))

def profile(request):
	print("Profile page hit from user: " + str(request.user))

	template = django.template.loader.get_template('newTwitter/profile.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))

def signinup(request):
	template = django.template.loader.get_template('newTwitter/signinup.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))

@login_required
def privateStuff(request):
	print("Luckily, the user " + str(request.user) + " is logged in")

	template = django.template.loader.get_template('newTwitter/privateStuff.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))

@login_required
def otherPrivateStuff(request):
	print("Luckily, the user " + str(request.user) + " is logged in")

	template = django.template.loader.get_template('newTwitter/otherPrivateStuff.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))