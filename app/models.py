from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
        USER = (
            (1,'HOD'),
            (2,'STAFF'),
            (3,'STUDENT'),
        )

        user_type = models.CharField(choices=USER, max_length=50,default=1)
        profile_pic = models.ImageField(upload_to = 'media/profile_pic')

class Course(models.Model):
        name = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

class Session_Year(models.Model):
        session_start = models.CharField(max_length=100)
        session_end = models.CharField(max_length=100)
        def __str__(self):
            return self.session_start + " to " + self.session_end



class Student(models.Model):
    # admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    student_regis = models.CharField(max_length=100)
    address = models.TextField(max_length=255,default='')
    gender = models.CharField(max_length=100)
    dob = models.DateField(default='')
    b_cnic = models.CharField(max_length=13,unique=True)
    father_name = models.TextField(max_length=100,default='')
    father_oc = models.TextField(max_length=100,null=False,default='', blank=True)
    father_mobile = models.TextField(max_length=11,default='')
    mother_name = models.TextField(max_length=100,null=True,default='', blank=True)
    mother_oc = models.TextField(max_length=100, null=True,default='', blank=True)
    mother_mobile = models.TextField(max_length=11,null=True, default='', blank=True)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year_id =models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    student_pic = models.ImageField(upload_to = 'media/student_pic',default='',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.b_cnic + ' ' + self.first_name + " " + self.last_name + " " + self.father_mobile