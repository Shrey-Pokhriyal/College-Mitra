from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    list_display= ['username','user_type']
        
        
admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(SessionYear)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(staff_notification)
admin.site.register(staff_leave)
admin.site.register(student_leave)
admin.site.register(student_notification)
admin.site.register(student_result)