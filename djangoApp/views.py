from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from djangoApp.models import School, Topic, Webpage, AccessRecord, User
from . import forms
from djangoApp.forms import NewUserForm
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, 
                                  DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

#Class based views

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'djangoApp/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'djangoApp/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    template_name = 'djangoApp/school_form.html'
    model = School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    template_name = 'djangoApp/school_form.html'
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('djangoApp:list')



class IndexView(TemplateView):
    template_name = 'djangoApp/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

'''
class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")

#Function based views
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'djangoApp/index.html', context=date_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'djangoApp/users.html', context=user_dict)
'''

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'djangoApp/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.USerProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.USerProfileInfoForm()
    
    return render(request, 'djangoApp/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
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
'''