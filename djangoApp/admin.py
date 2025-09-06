from django.contrib import admin
from djangoApp.models import Topic, Webpage, AccessRecord, User
from djangoApp.models import UserProfileInfo


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
#admin.site.register(User)
admin.site.register(UserProfileInfo)
# Register your models here.
