# Generated by Django 4.2.7 on 2024-03-22 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0057_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 17, 41, 18, 464022, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
    ]
