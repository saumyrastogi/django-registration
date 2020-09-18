from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from newapp.models import UserProfileInfo,User
from django.conf import settings
from django.conf.urls.static import static
from newapp.forms import UserForm,UserProfileInfoForm
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout

# Create your views here.

def home(request):
    return render(request,'newapp/Home.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def specialpage(request):
    username = request.user.username
    return render(request,'newapp/profile.html',{'username':username})


def register(request):

    registered = False


    if request.method=="POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile = profile_form.save()
            registered = True

        else:
            print("ERROR")



    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'newapp/register.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})


def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Login')

    else:
        return render(request,'newapp/login.html',{})
