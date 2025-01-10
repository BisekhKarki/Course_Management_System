from django.shortcuts import render,redirect
from .froms import CreateUserForm,LoginUserForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Course_Available,Instructor_Available,Student


# Create your views here
# User Dashboard
@login_required(login_url='login')
def Home(request):
    student = Student.objects.all().count()
    teacher = Instructor_Available.objects.all().count()
    course = Course_Available.objects.all().count()
    return render(request,'home.html',{
        'student':student,
        'teacher':teacher,
        'course':course
    })


# Logout a user
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged Out")
    return redirect('login')

# Login a user
def login_user(request):
    form = LoginUserForm()
    if request.method == "POST":
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                messages.success(request,"You have been logged In")
                login(request,user)
                return redirect('home')
    context = {
        'form':form
    }
    return render(request,'login.html',context)


# Register a user
def Signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully")
            return redirect('home')
    context = {
        'form':form
    }

    return render(request,'register.html',context)



# Create,edit,delete a course
def show_courses(request):
    courses = Course_Available.objects.all()
    return render(request,'Courses.html',{
        'courses':courses
    })

def edit_courses(request):
    return render(request,'Courses.html')


def add_courses(request):
    return render(request,'Courses.html')

def delete_courses(request):
    return render(request,'Courses.html')






