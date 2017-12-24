import django
from django.shortcuts import render

def handler400(request, exception):
	print("400 page hit from user: " + str(request.user))

	template = django.template.loader.get_template('conVerse/errorPages/400.html')
	context = {}
	return django.http.HttpResponseBadRequest(template.render(context, request))

def handler403(request, exception):
    print("403 page hit from user: " + str(request.user))

    template = django.template.loader.get_template('conVerse/errorPages/403.html')
    context = {}
    return django.http.HttpResponseForbidden(template.render(context, request))

def handler404(request, exception):
    print("404 page hit from user: " + str(request.user))

    template = django.template.loader.get_template('conVerse/errorPages/404.html')
    context = {}
    return django.http.HttpResponseNotFound(template.render(context, request))

def handler500(request, exception):
	print("500 page hit from user: " + str(request.user))

	template = django.template.loader.get_template('conVerse/errorPages/500.html')
	context = {}
	return django.http.HttpResponseServerError(template.render(context, request))