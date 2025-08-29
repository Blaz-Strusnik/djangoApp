from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insertMe': "Hello I am from views.py!"}
    return render(request, 'djangoApp/index.html', context=my_dict)