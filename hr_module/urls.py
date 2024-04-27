from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', employee_leave_balance, name='employee_leave_balance'),
    path('leave-requests/', leave_requests_list, name='leave_requests_list'),
    path('hp/', hr_homepage, name='hr_homepage'),
    path('<int:leave_request_id>/', manage_leave_request, name='manage_leave_request'),
]
