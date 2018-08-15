from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hi there, let's make this worthwile")


def about(request):
    return HttpResponse("This is what we do")
