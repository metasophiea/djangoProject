import django, json
from .. import models

def safeInt(val):
	try:
		return int(val)
	except:
		return None

def getQuery(model,attribute,value):
	try:
		return  model.objects.get(**{attribute: value})
	except:
		return None


def getTweets(request):
	limit = 10
	outputArray = []
	defaultObject = {
		'authorName':'',
		'text':'',
		'upVotes':0,
		'downVotes':0
	}

	index = safeInt(request.GET.get('index'))
	startIndex = safeInt(request.GET.get('start'))
	endIndex = safeInt(request.GET.get('end'))

	if index is not None:
		item = getQuery(models.tweet.tweet, 'tweetId', index)
		if item is not None:
			tempObject = dict(defaultObject)
			tempObject['authorName'] = item.author
			tempObject['text'] = item.text
			tempObject['upVotes'] = item.upVotes
			tempObject['downVotes'] = item.downVotes
			outputArray.append(tempObject)
		return django.http.HttpResponse( json.dumps(outputArray) )

	if startIndex is None and endIndex is None:
		# get all tweets
		for item in models.tweet.tweet.objects.all():
			tempObject = dict(defaultObject)
			tempObject['authorName'] = item.author
			tempObject['text'] = item.text
			tempObject['upVotes'] = item.upVotes
			tempObject['downVotes'] = item.downVotes
			outputArray.append(tempObject)
	elif startIndex is not None and endIndex is None:
		# get the tweets after and including startIndex
		items = models.tweet.tweet.objects.filter(tweetId__gte=startIndex, tweetId__lte=(startIndex+limit))
		for item in items:
			tempObject = dict(defaultObject)
			tempObject['authorName'] = item.author
			tempObject['text'] = item.text
			tempObject['upVotes'] = item.upVotes
			tempObject['downVotes'] = item.downVotes
			outputArray.append(tempObject)

	elif startIndex is None and endIndex is not None:
		# get the tweets before and including endIndex 
		items = models.tweet.tweet.objects.filter(tweetId__gte=(endIndex-limit), tweetId__lte=endIndex)
		for item in items:
			tempObject = dict(defaultObject)
			tempObject['authorName'] = item.author
			tempObject['text'] = item.text
			tempObject['upVotes'] = item.upVotes
			tempObject['downVotes'] = item.downVotes
			outputArray.append(tempObject)
	else:
		# get the tweets between and including startIndex and endIndex 
		if endIndex > (startIndex+limit):
			endIndex = startIndex+limit
		items = models.tweet.tweet.objects.filter(tweetId__gte=startIndex, tweetId__lte=endIndex)
		for item in items:
			tempObject = dict(defaultObject)
			tempObject['authorName'] = item.author
			tempObject['text'] = item.text
			tempObject['upVotes'] = item.upVotes
			tempObject['downVotes'] = item.downVotes
			outputArray.append(tempObject)
		pass

	return django.http.HttpResponse( json.dumps(outputArray) )