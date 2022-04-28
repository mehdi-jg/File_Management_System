from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

def index(request):
    return HttpResponse("Home page created for first time")

