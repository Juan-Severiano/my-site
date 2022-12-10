from django.http import HttpResponse

# Create your views here.

def my_view(request):
    return HttpResponse('sobre')

def home(request):
    return HttpResponse('Home')

def contato(request):
    return HttpResponse('contato')
