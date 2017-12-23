import django, json
from .. import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def api_updateScreenname(request):
    query = models.userdata.userdata.objects.get(username=request.user)
    query.screenname = request.POST['screenname']
    query.save()

    return redirect('profile')