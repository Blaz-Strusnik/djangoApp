from django.shortcuts import render
from django.http import HttpResponse
from djangoApp.models import Topic, Webpage, AccessRecord, User

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'djangoApp/index.html', context=date_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'djangoApp/users.html', context=user_dict)