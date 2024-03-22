from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html



class Category(models.Model):
    title = models.CharField(max_length=70, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دسته بندی')
    
    
    def get_absolute_url(self):
        return reverse('blog_app:category_detail', args=[self.id])
    
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    
     
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    category = models.ManyToManyField(Category, related_name="articles", verbose_name='دسته بندی')
    body = models.TextField(verbose_name='بدنه')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')
    pub_date = models.DateField(default=timezone.now(), verbose_name='تاریخ نشر')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    slug = models.SlugField(null=True, blank=True, unique=True, verbose_name='اسلاگ')
    
    
    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" alt="" width="80px" height="50px">')
        return format_html('<h3 style="color:red">تصویر ندارد</h3>')
    show_image.short_description = 'تصویر'
    
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)
        
    
    def get_absolute_url(self):
        return reverse('blog_app:article_detail', args=[self.slug])
    
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]}..."
    
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='کامنت والد')
    body = models.TextField(max_length=700, verbose_name='بدنه')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد کامنت')
    
    
    def __str__(self):
        return self.body[0:50]
    
    
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
    
    
    
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
        
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مفاله')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.article.title}'
    
    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)
        
        
class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='اینستاگرام')
    telegram = models.CharField(max_length=200, verbose_name='تلگرام')
    whatsapp = models.CharField(max_length=200, verbose_name='واتساپ')
    
    
    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'
        
    
    
        
    