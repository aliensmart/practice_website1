from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#user will inherit everything from the User class (username, firstname, password, email, lastname)

    #Additional data to add
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank=True)


    def __str__(self):
        return self.user.name
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(model.Model):
    full_name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


