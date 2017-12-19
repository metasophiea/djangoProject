import django
from django.shortcuts import render

def index(request):
	print("Main page hit from user: " + str(request.user))

	return django.http.HttpResponse( "- the site -" )