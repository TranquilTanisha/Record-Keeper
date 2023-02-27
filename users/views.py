from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm

def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=="POST":
        username=request.POST['username'].lower()
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, "Username or password is incorrect")

    context={}
    return render(request, 'users/login-register.html', context)

def registerUser(request):
    page='register'
    form=CustomUserCreationForm()

    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            #messages.success(request, "User account was created")
            login(request, user)
            return redirect('profile')

        else:
            messages.info(request, "An error has occured during registration")

    context={'page':page, "form":form}
    return render(request, 'users/login-register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    context={'profile':profile}
    return render(request, "users/account.html", context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=="POST":
        form=ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request, "users/profile_form.html", context)