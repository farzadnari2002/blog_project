from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='profile/image', null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username

