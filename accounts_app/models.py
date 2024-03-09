from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='کاربر')
    image = models.ImageField(upload_to='profile/image', null=True, blank=True, default="images\icons\profile.png", verbose_name='تصویر')
    
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

