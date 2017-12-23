import django, json
from itertools import count,  filterfalse
from .. import models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def updatePosition(verseObject):
    # gather all positions as a flat query array, excluding the working verse (because maybe this is the best spot)
    # add zero to that set, because we don't want any of them to be in that position
    # find the smallest available position
    A = set( models.verse.verse.objects.filter().exclude(position=verseObject.position).values_list('position', flat=True) )
    A.add(0)
    newPosition = next(filterfalse(A.__contains__, count(1)))

    # only if it's worthwhile; update the verse's position data
    if newPosition != verseObject.position:
        verseObject.position = newPosition
        verseObject.save()


@login_required
def api_updatePosition(request):
    # if the user has a verse; run the update code
    try:    updatePosition(models.verse.verse.objects.get(allauthUser=request.user))
    except: pass
    return redirect('profile')

@login_required
def api_updateVerse(request):
    try:
        # update verse
        verse = models.verse.verse.objects.get(allauthUser=request.user)
        verse.text = request.POST['verseText']
        if len(verse.text) == 0:
            verse.delete()
        else:
            verse.save()
    except:
        # create verse
        verse = models.verse.verse.objects.create(
            allauthUser=request.user,
            position=0,
            text=request.POST['verseText'],
            upVotes=0,
            downVotes=0
        )
        verse.save()

        updatePosition(verse)

    return redirect('profile')
