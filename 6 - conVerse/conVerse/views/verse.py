import django
from django.shortcuts import render

def verse(request):
	print("Verse page hit from user: " + str(request.user))

	return django.http.HttpResponse( "- the verse site -" )