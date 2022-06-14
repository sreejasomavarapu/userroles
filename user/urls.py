from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home),
    path('login/',loginpage,name='login'),
    path('register/',register,name='register'),
    path('volunteer/',volunteer,name='volunteer'),
    path('admin2/',admin,name='admin2'),
    path('coordinator/',coordinator,name='coordinator'),
    path('home-home/',home_home,name='home-home'),
    

]
