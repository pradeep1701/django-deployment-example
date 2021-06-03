from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofileinfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portofolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='Profile_pics', blank=True)

    def __str__(self):
        return self.user.username
