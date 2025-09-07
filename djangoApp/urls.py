from django.urls import path, re_path
from djangoApp import views 

app_name = 'djangoApp'

urlpatterns = [
    #re_path(r'^$', views.index, name='index'),
    #re_path(r'users/', views.users, name='users'),
    #re_path(r'formpage/', views.form_name_view, name='form_name'),
    re_path(r'register/', views.register, name='register'),
    re_path(r'user_login/', views.user_login, name='user_login'),
    re_path(r'logout/', views.user_logout, name='logout'),

]