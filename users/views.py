from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from .utils import searchProfiles

def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('account')

    if request.method=="POST":
        username=request.POST['username']
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

    return render(request, 'users/login-register.html')

def registerUser(request):
    page='register'
    form=CustomUserCreationForm()

    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username
            user.email=user.email
            user.first_name=user.first_name
            user.save()

            #messages.success(request, "User account was created")
            login(request, user)
            return redirect('account')

        else:
            messages.info(request, "An error has occured during registration")

    context={'page':page, "form":form}
    return render(request, 'users/login-register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('login')



def profiles(request):
    profiles=Profile.objects.all()
    profiles,search_query=searchProfiles(request)
    context={'profiles':profiles, 'search_query':search_query}
    return render(request, "users/profiles.html", context)

def userprofile(request, pk):
    profile=Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request, "users/user-profile.html", context)

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
