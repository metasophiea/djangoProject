import django, json
from .. import models

def safeInt(val):
	try:    return int(val)
	except: return None

def safeGetQuery(model,attribute,value):
	try:    return model.objects.get(**{attribute: value})
	except: return None


def getTweets(request):
# GET arguments: start, end, index

	# maximum number of tweets that can be requested
	limit = 10

	# harvest GET arguments
	index = safeInt(request.GET.get('index'))
	startIndex = safeInt(request.GET.get('start'))
	endIndex = safeInt(request.GET.get('end'))

	# perform the correct query depending on what arguments were used
	if index is not None:
		# get one specific tweet
		items = [safeGetQuery(models.tweet.tweet, 'tweetId', index)]
	elif startIndex is None and endIndex is None:
		# get first 'limit' tweets
		items = models.tweet.tweet.objects.filter(tweetId__gte=0, tweetId__lte=limit)
	elif startIndex is not None and endIndex is None:
		# get the tweets after and including startIndex
		items = models.tweet.tweet.objects.filter(tweetId__gte=startIndex, tweetId__lte=(startIndex+limit))
	elif startIndex is None and endIndex is not None:
		# get the tweets before and including endIndex 
		items = models.tweet.tweet.objects.filter(tweetId__gte=(endIndex-limit), tweetId__lte=endIndex)
	else:
		# get the tweets between and including startIndex and endIndex
		items = models.tweet.tweet.objects.filter(tweetId__gte=startIndex, tweetId__lte=(endIndex if endIndex <= (startIndex+limit) else (startIndex+limit)))

	# processes tweet objects into a mould for the JSON converter
	outputArray = []
	objectMould = {
		'authorName':'',
		'text':'',
		'upVotes':0,
		'downVotes':0
	}
	for item in items:
		tempObject = dict(objectMould)
		tempObject['authorName'] = item.author
		tempObject['text'] = item.text
		tempObject['upVotes'] = item.upVotes
		tempObject['downVotes'] = item.downVotes
		outputArray.append(tempObject)
	
	# convert array to a JSON string, package as a http response and return
	return django.http.HttpResponse( json.dumps(outputArray) )