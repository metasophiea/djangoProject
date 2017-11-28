import django, json
from .. import models

def getTweets(request):
	outputArray = []
	defaultObject = {
		'authorName':'',
		'text':'',
		'upVotes':0,
		'downVotes':0
	}

	for item in models.tweet.objects.all():
		tempObject = dict(defaultObject)
		tempObject['authorName'] = item.author
		tempObject['text'] = item.text
		tempObject['upVotes'] = item.upVotes
		tempObject['downVotes'] = item.downVotes
		outputArray.append(tempObject)

	return django.http.HttpResponse( json.dumps(outputArray) )