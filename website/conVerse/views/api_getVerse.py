import django, json
from .. import models

def safeInt(val):
	try:    return int(val)
	except: return None

def getVerseData(limit, index=None, start=None, end=None):
    basicQuery = models.verse.verse.objects

    # perform the correct query depending on what arguments were used
    if index is not None:
    	# get one specific verse
    	items = basicQuery.filter(position__gte=index, position__lte=index)
    elif start is None and end is None:
    	# get first 'limit' verses
    	items = basicQuery.filter(position__gte=0, position__lte=limit)
    elif start is not None and end is None:
    	# get the verses after and including start
    	items = basicQuery.filter(position__gte=start, position__lte=(start+limit))
    elif start is None and end is not None:
    	# get the verses before and including end 
    	items = basicQuery.filter(position__gte=(end-limit), position__lte=end)
    else:
    	# get the verses between and including start and end
        if end < start or end > (start+limit):
            end = (start+limit)
        items = basicQuery.filter(position__gte=start, position__lte=end)    

    return items.select_related('allauthUser__userdata')

def api_getVerse(request, index=None, start=None, end=None):
    limit = 8

    outputArray = []
    objectMould = {
    	'username':'',
    	'screenname':'',
    	'position':'',
    	'text':'',
    }
    for item in getVerseData(limit, safeInt(index), safeInt(start), safeInt(end)):
        tempObject = dict(objectMould)
        tempObject['username'] = item.allauthUser.username
        tempObject['screenname'] = item.allauthUser.userdata.screenname
        tempObject['position'] = item.position
        tempObject['text'] = item.text
        outputArray.append(tempObject)  

    return django.http.HttpResponse( json.dumps(outputArray) )