import django, json
from django.contrib.auth.decorators import login_required
from .models import verse

def getData(request):
    obj = {}
    obj["chunkOne"] = 1234567890
    obj["chunkTwo"] = [1,2,3,4,5,6,7,8,9,0]
    return django.http.HttpResponse( json.dumps(obj) )

def getVerses(request):
    outputArray = []
    dafaultObject = {
        "authorName":"",
        "text":"",
        "position":0,
        "upvotes":0,
        "downvotes":0
    }

    for item in verse.objects.all():
        tempObj = dict(dafaultObject)
        tempObj["authorName"] = item.author
        tempObj["text"] = item.text
        tempObj["position"] = item.position
        tempObj["upvotes"] = item.upvotes
        tempObj["downvotes"] = item.downvotes
        outputArray.append( tempObj )

    return django.http.HttpResponse( json.dumps(outputArray) )

@login_required
def index(request):
    if request.user.is_authenticated:
        print("I know this guy")
        print(request.user)
    else:
        print("just some user")
        print(request.user)

    template = django.template.loader.get_template('continuousVerse/index.html')
    context = {}
    return django.http.HttpResponse(template.render(context, request))

def login(request):
    if request.user.is_authenticated:
        print("wait...I know this guy! go back to the main page")
        print(request.user)
        return django.http.HttpResponseRedirect("/")

    template = django.template.loader.get_template('continuousVerse/login.html')
    context = {}
    return django.http.HttpResponse(template.render(context, request))

@login_required
def logout(request):
    return django.http.HttpResponse( "<script>location.href = \"/processLogout.exe\";</script>" )




def processLogin(request):
    print("starting login function")
    print(request.POST)
    print("authenticating...")
    user = django.contrib.auth.authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        print("login recognized")
        print(user)
        django.contrib.auth.login(request, user)
    else:
        print("login not recognized")

    return django.http.HttpResponseRedirect("/")

def processLogout(request):
    print("starting logout function")
    print(request.POST)
    print("logging out:",request.user)
    django.contrib.auth.logout(request)
    return django.http.HttpResponseRedirect("/")