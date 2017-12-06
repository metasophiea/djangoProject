import django
from django.shortcuts import render

import utilityCode

def index(request):
	print("Main page hit from user: " + str(request.user))

	utilityCode.mail.sendMail(
		"serverLog@metasophiea.com",
		"serverLog_reciever@metasophiea.com",
		"Main page hit from user: " + str(request.user),
		'newTwitter/index.html')

	template = django.template.loader.get_template('newTwitter/index.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))