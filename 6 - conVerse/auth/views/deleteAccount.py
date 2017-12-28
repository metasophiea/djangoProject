import django
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def deleteAccount(request):
	if 'deleteAccountConfirmation' in request.POST:
		# do it
		request.user.delete()
		return redirect('/')

	template = django.template.loader.get_template('account/account_delete.html')
	context = {}
	return django.http.HttpResponse(template.render(context, request))
