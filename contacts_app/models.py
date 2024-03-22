from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    created_an = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ دریافت پیغام')
    
    
    def __str__(self):
        return f'{self.title}-{self.text[:50]}'
    
    
    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'
        
        
class Contact(models.Model):
    address = models.TextField(verbose_name='آدرس')
    number = models.CharField(max_length=11, verbose_name='شماره همراه')
    email = models.EmailField(verbose_name='ایمیل')
    instagram = models.URLField(max_length=200, verbose_name='اینستاگرام')
    telegram = models.URLField(max_length=200, verbose_name='تلگرام')
    whatsapp = models.URLField(max_length=200, verbose_name='واتساپ')
    
    
    class Meta:
        verbose_name = 'پل ارتباطی'
        verbose_name_plural = 'پل های ارتباطی'
        
    