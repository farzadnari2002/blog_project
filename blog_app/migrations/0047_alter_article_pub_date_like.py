# Generated by Django 4.2.7 on 2024-03-10 12:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0046_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 10, 12, 7, 58, 402986, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog_app.article', verbose_name='مفاله')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'لایک',
                'verbose_name_plural': 'لایک ها',
                'ordering': ('-created_at',),
            },
        ),
    ]
