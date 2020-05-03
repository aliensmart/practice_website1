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
    if request.methode == 'POST':
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