import django, json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
	print("Main page hit from user: " + str(request.user))

	template = django.template.loader.get_template('newTwitter/index.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))

def getTweets(request):
	outputArray = []
	defaultObject = {
		'authorName':'',
		'text':'',
		'upVotes':0,
		'downVotes':0
	}

	for item in tweet.objects.all():
		tempObject = dict(defaultObject)
		tempObject['authorName'] = item.author
		tempObject['text'] = item.text
		tempObject['upVotes'] = item.upVotes
		tempObject['downVotes'] = item.downVotes
		outputArray.append(tempObject)

	return django.http.HttpResponse( json.dumps(outputArray) )

def login(request):
	if request.method == 'POST':
		user = django.contrib.auth.authenticate(
			username = request.POST['username'],
			password = request.POST['password']
		)

		if user:
			django.contrib.auth.login(request, user)

		return django.http.HttpResponseRedirect('/')
	else:
		if request.user.is_authenticated:
			print("wait, I know " + str(request.user) + ", send them back to the homepage")
			return django.http.HttpResponseRedirect("/")

		template = django.template.loader.get_template('newTwitter/login.html')
		context = {}
		return django.http.HttpResponse(template.render(context, request))

@login_required
def logout(request):
	django.contrib.auth.logout(request)
	return django.http.HttpResponseRedirect('/')