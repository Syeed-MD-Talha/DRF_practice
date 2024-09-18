from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views import View


# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

class SignInView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('home')
                # return render(request, 'home.html', {'user':username})
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    
class SignOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request,f'You have been logged out.')
        return redirect('home')  

class SignUp(View):
    def get(self,request):
        form=RegisterForm()
        return render(request, 'signup.html',{'form':form})
    def post(self,request):
        form=RegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to log in.')
            return redirect('home')
        return render(request, 'signup.html', {'form': form})