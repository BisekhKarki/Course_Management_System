from django.urls import path
from . import views

urlpatterns = [
    path('teacher/',views.show_teacher,name='teacher')
]