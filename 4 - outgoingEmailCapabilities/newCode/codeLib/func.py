import django

def index(request):
    return django.http.HttpResponse( "Hello from codeLib/func" )