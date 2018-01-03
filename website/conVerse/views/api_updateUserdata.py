import django, json
from .. import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def api_updateScreenname(request):
    # make sure that the new screenname isn't bigger than what the model allows
    if len(request.POST['screenname']) > models.userdata.userdata._meta.get_field('screenname').max_length:
        return redirect('profile')

    query = models.userdata.userdata.objects.get(username=request.user)
    query.screenname = request.POST['screenname']
    query.save()

    return redirect('profile')