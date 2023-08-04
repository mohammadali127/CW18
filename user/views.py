from django.shortcuts import render, redirect
from .forms import CreateUser

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            todo.objects.create(title=cd['title'], body=cd['body'], created_at=cd['created'])
            messages.success(request, 'todo was created successfully', 'success')
            return redirect('home')
    form = TodoCreateForm()
    return render(request, 'create.html', {'form':form})

def update(request, todo_id):
    pass