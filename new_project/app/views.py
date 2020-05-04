from django.shortcuts import render
from .forms import UserForm, ProfileData

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
        return render(request, 'login.html')

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
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

                registered = True
        else:
            print(user_form.errors, profile_data.errors)
    
    else:
        user_form = UserForm
        profile_data = ProfileData
    
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_data': profile_data,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'app/school_details.html'

class SchoolCreate(CreateView):
    fields = ('name', 'principal', 'location', 'contact')
    model = models.School

class SchoolUpdate(UpdateView):
    fields = ('name', 'principal', 'contact')
    model = models.School

class SchoolDelete(DeleteView):
    model = models.School
    success_url = reverse_lazy('app:list')
    
