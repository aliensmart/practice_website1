from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#user will inherit everything from the User class (username, firstname, password, email, lastname)

    #Additional data to add
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank=True)


    def __str__(self):
        return self.user.name



