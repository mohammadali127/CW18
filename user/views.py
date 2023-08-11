from django.shortcuts import render, redirect
from .forms import CreateUser
from .models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'todo was created successfully', 'success')
            return redirect('home')
    form = CreateUser()
    return render(request, 'create.html', {'form':form})

def UpdateTaskView
