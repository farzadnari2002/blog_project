# Generated by Django 4.2.7 on 2024-03-22 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0049_alter_socialmedia_options_alter_article_pub_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 11, 11, 41, 489224, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
    ]
