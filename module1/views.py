from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave
from .forms import LeaveForm
from django.contrib.auth.models import User,auth
from django.contrib import messages


def leave_request(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave_request.html', {'form': form})

def leave_list(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'leave_list.html', {'leaves': leaves})

def homepage(request):
    return render(request,'homepage.html')


