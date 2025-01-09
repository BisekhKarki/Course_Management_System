from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
]