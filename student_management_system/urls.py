"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# after creating folder of static import these settings

from django.conf import settings
from django.conf.urls.static import static

from .import views,hod_views,staff_views,student_views



urlpatterns = [

    path("admin/", admin.site.urls),
    path('base/',views.BASE,name='base'),

#login path

    path('', views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

# profile update

    path('profile/',views.PROFILE, name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),
# this is HOD panel url

    path('hod/home',hod_views.HOME,name='hod_home'),
    path('hod/student/add',hod_views.AddStudent,name='add_student'),
    path('hod/student/view',hod_views.VIEW_STUDENT,name='view_student'),
    path('hod/student/edit/<str:id>',hod_views.EDIT_STUDENT, name='edit_student'),
    # path('hod/student/update/',hod_views.UPDATE_STUDENT, name='update_student'),
    path("delete/<int:id>",hod_views.student_delete , name ='delete'),

    # add class paths
    path('hod/class/add',hod_views.AddCourse,name='add_course'),
    path('hod/class/view',hod_views.ViewCourse,name='view_course_edit'),
    path('hod/class/view',hod_views.ViewCourse,name='view_course_del'),
    path('hod/class/view',hod_views.ViewCourse,name='view_course'),
    path('hod/class/edit/<str:id>',hod_views.EDIT_COURSE, name='edit_course'),
    path('hod/class/update/',hod_views.UPDATE_COURSE, name='update_course'),
    path("delete/class/<int:id>",hod_views.course_delete , name ='delete_c'),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
