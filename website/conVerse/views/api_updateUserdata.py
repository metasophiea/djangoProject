import django, json
from .. import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def api_updateScreenname(request):
    query = models.userdata.userdata.objects.get(username=request.user)
    query.screenname = request.POST['screenname']

    # make sure that the new screenname isn't bigger than what the model allows
    if len(query.screenname) <= models.userdata.userdata._meta.get_field('screenname').max_length:
        query.save()

    return redirect('profile')