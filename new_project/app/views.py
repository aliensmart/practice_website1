from django.shortcuts import render
from .forms import UserForm, ProfileData

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        username = request.POST.get('username')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account does not Exist or inactive")
            
        else:
            return HttpResponse("Invalid Login detail")

    else:
        return render(request, 'app/login.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_data = ProfileData(data=request.POST)

        if user_form.is_valid() and profile_data.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_data.save(commit=False)
            profile.save()

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

                registered = True
        else:
            print(user_form.errors, profile_data.errors)
    
    else:
        user_form = UserForm
        profile_data = ProfileData
    
    return render(request, 'app/register.html',
                  {'user_form': user_form,
                   'profile_data': profile_data,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
        