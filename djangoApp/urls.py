from django.urls import path, re_path
from djangoApp import views 

app_name = 'djangoApp'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'users/', views.users, name='users'),
    re_path(r'formpage/', views.form_name_view, name='form_name'),
]