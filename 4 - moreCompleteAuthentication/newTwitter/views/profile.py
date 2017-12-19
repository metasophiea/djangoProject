import django, json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import data
from .. import models

@login_required
def main(request):
    print("Profile page hit from user: " + str(request.user))

    items = data.getTweets_byAuthorId(request.user)
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





    template = django.template.loader.get_template('newTwitter/profile.html')
    context = {
        'user':request.user,
        'tweets':json.dumps(outputArray)
    }
    return django.http.HttpResponse(template.render(context, request))

@login_required
def submitTweet(request):
    returnText='Done'
    print()
    print("---- ----")
    if request.POST.get('submit'):
        print("- a request was made to create a tweet -")
        print('tweetId:', request.POST['tweetId'])
        print('text:', request.POST['text'])
        print('author:', request.POST['author'])
        print()
        print("by the user:", request.user.username)
        print()

        try:
            item = models.tweet.tweet.objects.get(tweetId=request.POST['tweetId']) 
            # does the user own this tweet?
            if item.authorId == request.user:
                print("this tweet already exists, so we're going to update it")
                print("currently:", item, ' - ', item.text)
                item.text = request.POST['text']
                item.save()
            else:
                returnText = 'error: not your tweet!'

        except:
            print("this tweet does not exist, so we're going to make it")
            item = models.tweet.tweet.objects.create(
                tweetId=request.POST['tweetId'],
                authorId=request.user,
                author= request.POST['author'],
                text=request.POST['text']
            )
            item.save()
    elif request.POST.get('delete'):
        print("- a request was made to delete a tweet -")
        print('tweetId:', request.POST['tweetId'])
        print('text:', request.POST['text'])
        print('author:', request.POST['author'])
        print()
        print("by the user:", request.user.username)
        print()

        try:
            item = models.tweet.tweet.objects.get(tweetId=request.POST['tweetId'])
            # does the user own this tweet?
            if item.authorId == request.user:
                item.delete()
            else:
                returnText = 'error: not your tweet!'

        except:
            pass

        print("tweet deleted")
    else:
        print("unknown action")


    print("---- ----")
    print()
    return django.http.HttpResponse(returnText)

