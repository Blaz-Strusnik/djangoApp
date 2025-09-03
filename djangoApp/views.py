from django.shortcuts import render
from django.http import HttpResponse
from djangoApp.models import Topic, Webpage, AccessRecord, User
from . import forms
from djangoApp.forms import NewUserForm
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'djangoApp/index.html', context=date_dict)
'''
def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'djangoApp/users.html', context=user_dict)
'''
def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error: Form Invalid")
    return render(request, 'djangoApp/users.html', {'form': form}) 


def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            print("Validation Success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
    
    return render(request, 'djangoApp/form_page.html', {'form': form})