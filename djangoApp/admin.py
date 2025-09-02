from django.contrib import admin
from djangoApp.models import Topic, Webpage, AccessRecord, User

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
# Register your models here.
