from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Home page created for first time")

