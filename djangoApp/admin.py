from django.contrib import admin
from djangoApp.models import Topic, Webpage, AccessRecord, UserProfileInfo, School, Student, User



admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
#admin.site.register(User)
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)
# Register your models here.
