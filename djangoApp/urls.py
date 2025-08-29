from django.urls import path, re_path
from djangoApp import views 

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]