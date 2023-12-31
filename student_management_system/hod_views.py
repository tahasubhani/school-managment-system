from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Session_Year, CustomUser,Student,Section
from django.contrib import messages
from django.db.models import Max

@login_required(login_url='/')
def HOME(request):
    return render(request,'hod/home.html')



# add student function
@login_required(login_url='/')
def AddStudent(request):
    regis = 000 if Student.objects.count() == 0 else Student.objects.aggregate(max=Max('student_regis'))["max"]+1
    # print(regis)
    section = Section.objects.all()
    # print(section)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    # print(course)
    # print(session_year)
    # try:
    #     student = Student.objects.create(student_regis=regis)
    #     error = 'no'
    # except:
    #     error = 'yes'

    if request.method == 'POST':
      
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        course_id = request.POST.get('course_id')
        section_id = request.POST.get('section_id')
        session_year_id = request.POST.get('session_year_id')
        b_cnic = request.POST.get('b_cnic')
        student_pic = request.FILES.get('student_pic')
        father_name = request.POST.get('father_name')
        father_oc = request.POST.get('father_oc')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_oc = request.POST.get('mother_oc')
        mother_mobile = request.POST.get('mother_mobile')
        address = request.POST.get('address')
        # print(first_name,last_name,student_regis,gender,dob,course_id,b_cnic,session_year_id,section,student_pic,father_name,father_oc,father_mobile,mother_name,mother_oc,mother_mobile,address)
        if Student.objects.filter(b_cnic=b_cnic).exists():
            messages.warning(request,'Student is already registered in your account')
            return redirect('add_student')
        else:
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                messages.error('value does not exist')
                return redirect('add_student')
            # try:
            #     section = Section.objects.get(id=section_id)
            # except Section.DoesNotExist:
            #     messages.error('value does not exist')
            #     return redirect('add_student')
            session_year = Session_Year.objects.get(id=session_year_id)
            section = Section.objects.get(id=section_id)
            

            student = Student(
               first_name = first_name,
               last_name = last_name,
               student_regis = regis,
               gender = gender,
               dob = dob,
               course_id = course,
               section_id = section,
               b_cnic = b_cnic,
               session_year_id = session_year,
               student_pic = student_pic,
               father_name = father_name,
               father_oc = father_oc,
               father_mobile = father_mobile,
               mother_name = mother_name,
               mother_oc = mother_oc,
               mother_mobile =mother_mobile,
               address = address,
           )
            
            student.save()
            messages.success(request,'Student admitted Succcesfully')
        
        return redirect('add_student')
    context={
        'course': course,
        'session_year': session_year,
        'section': section,
        'student_regis': regis
    }
    return render(request,'hod/add_student.html',context)
def VIEW_STUDENT(request):
    student = Student.objects.all()
    # print(student)
    context={
        'student' : student,
    }
    return render(request,'hod/view_student.html',context)



def StudentDetails(request,id):
    student = Student.objects.get(b_cnic=id)
    # # print(student)
    course =Course.objects.all()
    session_year =Session_Year.objects.all()
    section = Section.objects.all()
    
    ##########################################################
    if request.method == 'POST':
        # student_id = request.POST.get('student_id')
        # print(student_id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_regis = request.POST.get('student_regis')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        course_id = request.POST.get('course_id')
        b_cnic = request.POST.get('b_cnic')
        session_year_id = request.POST.get('session_year_id')
        section_abc = request.POST.get('section_abc')
        student_pic = request.FILES.get('student_pic')
        father_name = request.POST.get('father_name')
        father_oc = request.POST.get('father_oc')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_oc = request.POST.get('mother_oc')
        mother_mobile = request.POST.get('mother_mobile')
        address = request.POST.get('address')

        
        try:
            student = Student.objects.get(b_cnic=id)
            student.first_name = first_name
            student.last_name =  last_name
            student.student_regis = student_regis
            student.gender = gender
            student.dob = dob
            # print(course_id)
            # student.course_id = Course.objects.all()
            student.b_cnic = b_cnic
            # student.session_year_id = Session_Year.objects.get(id=session_year_id)
            student.section_id = section_id
            # student.student_pic = student_pic
            if student_pic !=None and student_pic != '':
                student.student_pic = student_pic
            student.father_name = father_name
            student.father_oc = father_oc
            student.father_mobile = father_mobile
            student.mother_name = mother_name
            student.mother_oc = mother_oc
            student.mother_mobile = mother_mobile
            student.address = address

            student.save()
            messages.success(request,'Student profile Updated Successfully')
            return redirect('view_student')
        except Student.DoesNotExist:
            messages.error(request,'your Profile is not updated')



    ############################################################
    
    context = {
            'course': course,
            'session_year': session_year,
            'student':student,

        }
    return render(request,'hod/student_details.html',context)
# course =Course.objects.get(id=id)
    
#     context = {
            
#             'course': course,
            
#         }
#     return render(request,'hod/student_details.html',context)

def student_delete(request,id):

    student_del =Student.objects.get(b_cnic=id)
    student_del.delete()
    
    # student = Student.objects.filter( user = request.id,b_cnic=0)
    # if student.exists():
    messages.success(request,'Student Record deleted Successfully')
    return redirect('view_student')
    # else:
    #     return redirect('add_student')
    # # return redirect('add_student')

    
def EDIT_STUDENT(request,id):
    if request.method == 'POST':
        # student_id = request.POST.get('student_id')
        # print(student_id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_regis = request.POST.get('student_regis')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        course_id = request.POST.get('course_id')
        b_cnic = request.POST.get('b_cnic')
        session_year_id = request.POST.get('session_year_id')
        section_abc = request.POST.get('section_abc')

        student_pic = request.FILES.get('student_pic')
        father_name = request.POST.get('father_name')
        father_oc = request.POST.get('father_oc')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_oc = request.POST.get('mother_oc')
        mother_mobile = request.POST.get('mother_mobile')
        address = request.POST.get('address')

        
        try:
            student = Student.objects.get(b_cnic=id)
            student.first_name = first_name
            student.last_name =  last_name
            student.student_regis = student_regis
            student.gender = gender
            student.dob = dob
            # print(course_id)
            student.course_id = Course.objects.get(id=course_id)
            student.b_cnic = b_cnic
            student.session_year_id = Session_Year.objects.get(id=session_year_id)
            student.section_abc = section_abc
            
            # student.student_pic = student_pic
            if student_pic !=None and student_pic != '':
                student.student_pic = student_pic
            student.father_name = father_name
            student.father_oc = father_oc
            student.father_mobile = father_mobile
            student.mother_name = mother_name
            student.mother_oc = mother_oc
            student.mother_mobile = mother_mobile
            student.address = address

            student.save()
            messages.success(request,'Student profile Updated Successfully')
            return redirect('view_student')
        except Student.DoesNotExist:
            messages.error(request,'your Profile is not updated')
    student =Student.objects.filter(b_cnic=id)
    course =Course.objects.all()
    session_year =Session_Year.objects.all()
    context = {
            'student':student,
            'course': course,
            'session_year': session_year,
        }
    return render(request,'hod/edit_student.html',context)

# def UPDATE_STUDENT(request):
#      if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         student_regis = request.POST.get('student_regis')
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')
#         course_id = request.POST.get('course_id')
#         b_cnic = request.POST.get('b_cnic')
#         session_year_id = request.POST.get('session_year_id')
#             #    section = section,
#         student_pic = request.FILES.get('student_pic')
#         father_name = request.POST.get('father_name')
#         father_oc = request.POST.get('father_oc')
#         father_mobile = request.POST.get('father_mobile')
#         mother_name = request.POST.get('mother_name')
#         mother_oc = request.POST.get('mother_oc')
#         mother_mobile = request.POST.get('mother_mobile')
#         address = request.POST.get('address')
#         try:
#             student = Student.objects.get(b_cnic=id)
#             student.first_name = first_name
#             student.last_name =  last_name
#             student.student_regis = student_regis
#             student.gender = gender
#             student.dob = dob
#             print(course_id)
#             student.course_id = Course.objects.get(id=course_id)
#             student.b_cnic = b_cnic
#             student.session_year_id = Session_Year.objects.get(id=session_year_id)
#             student.student_pic = student_pic
#             student.father_name = father_name
#             student.father_oc = father_oc
#             student.father_mobile = father_mobile
#             student.mother_name = mother_name
#             student.mother_oc = mother_oc
#             student.mother_mobile = mother_mobile
#             student.address = address

#             student.save()
#             messages.success(request,'Student profile Updated Successfully')
#             return redirect('view_student')
#         except Student.DoesNotExist:
#             messages.error(request,'your Profile is not updated')
#         student =Student.objects.filter(b_cnic=id)
#         course =Course.objects.all()
#         session_year =Session_Year.objects.all()
#         context = {
#                  'student':student,
#                  'course': course,
#                 'session_year': session_year,}
#         return render(request,'hod/edit_student.html',context)
        
def AddCourse(request):
    if request.method == 'POST':
        name = request.POST['name']
        fee_course = request.POST['fee_course']
        # print(course_name)
        course = Course(
            name = name,
            fee_course = fee_course,
        )
        course.save()
        messages.success(request,'Class is Successfully Created')
        return redirect('add_course')
    return render(request,'hod/add_course.html')

    

def ViewCourse(request):
    course = Course.objects.all()
    # print(student)
    context={
        'course' : course,
    }
    return render(request,'hod/view_course.html',context)

def EDIT_COURSE(request,id):
    course =Course.objects.get(id=id)
    
    context = {
            
            'course': course,
            
        }
    return render(request,'hod/edit_course.html',context)

def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        fee_course = request.POST.get('fee_course')
        course_id = request.POST.get('course_id')
        # print(course_name,course_id)
        course = Course.objects.get(id=course_id)
        course.name = name
        course.fee_course = fee_course
        course.save()
        messages.success(request,'Class Name is Editted successfully')
        return redirect('view_course')
    return render(request,'hod/edit_course.html')

def course_delete(request,id):

    course_del =Course.objects.get(id=id)
    course_del.delete()
    messages.success(request,'Class is deleted Successfully')
    return redirect('view_course')

# function staff
def ADD_STAFF(request):
    return render(request,'hod/student_details.html')