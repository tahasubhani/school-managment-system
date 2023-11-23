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
        fee_course = models.CharField(max_length=100,default='', blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

class Section(models.Model):
    section_name = models.CharField(max_length=100)
    # fee_course = models.CharField(max_length=100,default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_name
class Session_Year(models.Model):
        session_start = models.CharField(max_length=100)
        session_end = models.CharField(max_length=100)
        def __str__(self):
            return self.session_start + " to " + self.session_end


class Student(models.Model):
    # admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    student_regis = models.IntegerField(null=True)
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
    section_id = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    

    def __str__(self):
            return self.b_cnic + ' ' + self.first_name + " " + self.last_name + " " + self.father_mobile
    
class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100)
    teacher_cnic = models.CharField(max_length=13,unique=True)
    address = models.TextField(max_length=255,default='')
    salary = models.CharField(max_length=100,default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher_pic = models.ImageField(upload_to = 'media/teacher_pic',default='',blank=True, null=True)
    joining_date = models.DateField(default='')
    qualification = models.CharField(max_length=100)
    cv_resume = models.FileField(upload_to = 'media/teacher_cv',default='',blank=True, null=True)
    
    


    def __str__(self):
          return self.teacher_cnic_cnic + ' ' + self.first_name + " " + self.last_name



# class CourseLecture(models.Model):
#     course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     lectures = models.ManyToManyField('Lecture')

#     def __str__(self):
#         return self.name

# class Lecture(models.Model):
#     course_lecture = models.ForeignKey(CourseLecture,on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     order = models.PositiveIntegerField()

#     def __str__(self):
#         return self.title
    
class FeePayment(models.Model):
    b_cnic = models.ForeignKey('b_cnic', on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True)
    date_of_payment = models.DateField()
    fee_type = models.CharField(max_length=100)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.b_cnic.name}'s payment for {self.fee_type} on {self.date_of_payment}"

class FeeType(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.name

class b_cnic(models.Model):
    b_cnic = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)
    class Meta:
        verbose_name_plural = 'b_cnic'

    def __str__(self):
        return self.b_cnic
    
