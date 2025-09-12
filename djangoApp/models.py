from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=264)
    principal = models.CharField(max_length=264)
    location = models.CharField(max_length=264)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("djangoApp:detail", kwargs={"pk": self.pk})
    
class Student(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
'''
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique=True)

'''


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username