from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(cd['username'], cd['email'], cd['first_name'], cd['last_name'], cd['password'])
            messages.success(request, 'you registered successfully', 'success')
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, password=cd['password'], username=cd['username'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('home')
            messages.error(request, 'username or password is wrong.', 'warning')
        return render(request, 'login.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        posts = Post.objects.filter(user=user)
        return render(request, 'account/profile.html', {'user': user, 'posts': posts})

class CreateTaskView(View):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'todo was created successfully', 'success')
            return redirect('home')
    form = CreateUser()
    return render(request, 'create.html', {'form':form})

class UpdateTaskView(View):
    pass
class UpdateProfileview(View):
    pass