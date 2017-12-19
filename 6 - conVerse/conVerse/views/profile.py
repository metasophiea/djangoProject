import django
from django.shortcuts import render

def profile(request):
	print("Profile page hit from user: " + str(request.user))

	return django.http.HttpResponse( "- the profile site -" )