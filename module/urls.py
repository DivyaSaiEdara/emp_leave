from django.urls import path
from .views import *

urlpatterns = [
    path('sign/',signup,name='signup'),
    path('sign1/',signup1,name='signup1'),
    path('l/',login,name='login'),
    path('l1/',login1,name='login1'),
    path('lg/',logout,name='logout'),
    path('',newhomepage,name='newhomepage'),
    path('h/',hr_homepage,name='hr_homepage'),
    path('e/',homepage,name='homepage'),
]