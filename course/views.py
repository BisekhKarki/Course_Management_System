from django.shortcuts import render,redirect
from .froms import CreateUserForm,LoginUserForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here
# User Dashboard
@login_required(login_url='login')
def Home(request):
    return render(request,'home.html')


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
