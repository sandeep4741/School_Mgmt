from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Student_Data, Teacher_Data, Student_Performance, Teacher_Performance


# Create your views here.
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # login authentication
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if username == 'principal':
                login(request, user)
                return render(request, 'principal.html')
            elif username == 'super':
                login(request, user)
                return render(request, 'super.html')
            else:
                login(request, user)
                return render(request, 'clerk.html')
        else:
            messages.success(request, 'invalid details')
            return redirect('login')


def studentdata_page(request):
    if request.method == 'GET':
        return render(request, 'studentdata.html')
    else:
        RollNumber_1 = request.POST['rollno']
        if Student_Data.objects.filter(RollNumber=RollNumber_1).exists():
            messages.error(request, "Roll Number already present!")
            return render(request, "studentdata.html")
        else:
            Student_Data(Student_Name=request.POST.get('name'),
                         Class=request.POST.get('class'),
                         RollNumber=request.POST.get('rollno'),
                         DateOfBirth=request.POST.get('dob'),
                         Gender=request.POST.get('gender'),
                         Address=request.POST.get('address')
                         ).save()
            return redirect('clerk')


def teacherdata_page(request):
    if request.method == 'GET':
        return render(request, 'teacherdata.html')
    else:
        teacher_id_1 = request.POST['teacher_id']
        if Teacher_Data.objects.filter(TeacherId=teacher_id_1).exists():
            messages.error(request, "Teacher Id already present!")
            return render(request, "teacherdata.html")
        else:
            Teacher_Data(Name=request.POST.get('name'),
                         TeacherId=request.POST.get('teacher_id'),
                         Qualification=request.POST.get('qualification'),
                         DateOfJoining=request.POST.get('doj'),
                         Gender=request.POST.get('gender'),
                         Subject=request.POST.get('subject')
                         ).save()
            return redirect('clerk')


def studentperform_page(request):
    if request.method == 'GET':
        return render(request, 'studentperform.html')
    else:
        rollno_1 = request.POST['rollno']
        if Student_Performance.objects.filter(RollNumber=rollno_1).exists():
            messages.error(
                request, "Roll Number already present already present!")
            return render(request, "studentperform.html")
        else:
            Student_Performance(Student_Name=request.POST.get('name'),
                                Class=request.POST.get('class'),
                                RollNumber=request.POST.get('rollno'),
                                Grade=request.POST.get('grade'),
                                Remarks=request.POST.get('remark')
                                ).save()
            return redirect('clerk')


def teacherperform_page(request):
    if request.method == 'GET':
        return render(request, 'teacherperform.html')
    else:
        teacherid_1 = request.POST['teacherid']
        if Teacher_Performance.objects.filter(TeacherId=teacherid_1).exists():
            messages.error(request, "Teacher Id already present")
            return render(request, "teacherperform.html")
        else:
            Teacher_Performance(Teacher_Name=request.POST.get('name'),
                                TeacherId=request.POST.get('teacherid'),
                                Subject=request.POST.get('subject'),
                                Remarks=request.POST.get('remark')
                                ).save()
            return redirect('clerk')


def clerk_page(request):
    return render(request, 'clerk.html')


# for clerk to display the data

def clerk_studentdata(request):
    studentdata_1 = Student_Data.objects.all()
    return render(request, 'clerkdisplay.html', {"studentdata": studentdata_1})


def clerk_studentperform(request):
    studentperform_1 = Student_Performance.objects.all()
    return render(request, 'clerkdisplay.html', {"studentperform": studentperform_1})


# for superintendent to display the data

def super_studentdata(request):
    studentdata_1 = Student_Data.objects.all()
    return render(request, 'super.html', {"studentdata": studentdata_1})


def super_studentperform(request):
    studentperform_1 = Student_Performance.objects.all()
    return render(request, 'super.html', {"studentperform": studentperform_1})


def super_teacherdata(request):
    teacherdata_1 = Teacher_Data.objects.all()
    return render(request, 'super.html', {"teacherdata": teacherdata_1})


# for principal to display the data

def principal_studentdata(request):
    studentdata_1 = Student_Data.objects.all()
    return render(request, 'principal.html', {"studentdata": studentdata_1})


def principal_studentperform(request):
    studentperform_1 = Student_Performance.objects.all()
    return render(request, 'principal.html', {"studentperform": studentperform_1})


def principal_teacherdata(request):
    teacherdata_1 = Teacher_Data.objects.all()
    return render(request, 'principal.html', {"teacherdata": teacherdata_1})


def principal_teacherperform(request):
    teacherperform_1 = Teacher_Performance.objects.all()
    return render(request, 'principal.html', {"teacherperform": teacherperform_1})
