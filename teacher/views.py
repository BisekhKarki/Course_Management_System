from django.shortcuts import render
from course.models import Instructor_Available


# Create your views here.

# Create,edit,delete a Teacher
def show_teacher(request):
    get_teacher_details = Instructor_Available.objects.all()
    return render(request,'Teacher.html',{
        'teachers':get_teacher_details
    })

def edit_teacher(request):
    return render(request,'Teacher.html')


def add_teacher(request):
    return render(request,'Teacher.html')

def delete_teacher(request):
    return render(request,'Teacher.html')

