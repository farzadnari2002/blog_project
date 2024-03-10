# Generated by Django 4.2.7 on 2024-03-09 14:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0043_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'پیغام', 'verbose_name_plural': 'پیغام ها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog_app.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/articles', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 9, 14, 24, 3, 623477, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=70, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=70, verbose_name='عنوان'),
        ),
    ]