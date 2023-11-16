from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    list_display = ['id','username','user_type','email']


# class StudentModel(UserAdmin):
#     list_display = ['id','b_cnic']

admin.site.register(CustomUser,UserModel) 
admin.site.register(Course) 
admin.site.register(Session_Year) 
admin.site.register(Student) 
