"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('clerk', views.clerk_page, name='clerk'),

    path('studententry', views.studentdata_page, name='studentdata_entry'),
    path('teacherentry', views.teacherdata_page, name='teacherdata_entry'),
    path('studentperform', views.studentperform_page,name='studentperform_entry'),
    path('teacherperform', views.teacherperform_page,name='teacherperform_entry'),

    path('clerkdisplay_sd', views.clerk_studentdata, name='clerk_studentdata'),
    path('clerkdisplay_sp', views.clerk_studentperform,name='clerk_studentperform'),

    path('superdisplay_sd', views.super_studentdata, name='super_studentdata'),
    path('superdisplay_sp', views.super_studentperform,name='super_studentperform'),
    path('superdisplay_td', views.super_teacherdata, name='super_teacherdata'),

    path('studentdisplay', views.principal_studentdata,name='principal_studentdata'),
    path('teacherdisplay', views.principal_teacherdata,name='principal_teacherdata'),
    path('studentperformdisplay', views.principal_studentperform,name='principal_studentperform'),
    path('teacherperformrdisplay', views.principal_teacherperform,name='principal_teacherperform'),

    # path('principal',views.principal_page,name='principal'),






]
