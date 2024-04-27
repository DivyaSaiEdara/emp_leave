from django.urls import path
from .views import *


urlpatterns = [
    path('request/', leave_request, name='leave_request'),
    path('list/', leave_list, name='leave_list'),
    path('hp/',homepage,name='homepage'),
]
