import django
from django.contrib.auth.decorators import login_required

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