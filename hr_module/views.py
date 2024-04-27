from django.shortcuts import render,redirect
from .models import Employee, LeaveRequest
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_leave_balance(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee_leave_balance.html', {'employee': employee})

def leave_requests_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_requests_list.html', {'leave_requests': leave_requests})



def approve_leave(request, request_id):
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Approved'
    leave_request.save()
    # Redirect to leave requests list after approval
    return redirect('leave_requests_list')

def reject_leave(request, request_id):
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Rejected'
    leave_request.save()
    # Redirect to leave requests list after rejection
    return redirect('leave_requests_list')

def hr_homepage(request):
    return render(request, 'hr_homepage.html')

def manage_leave_request(request, leave_request_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_request_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        leave_request.status = status
        leave_request.save()
        return redirect('leave_request_list')
    return render(request, 'leave_requests/manage_leave_request.html', {'leave_request': leave_request})
