# Generated by Django 4.2.7 on 2024-03-22 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0050_delete_message_alter_article_pub_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialMedia',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 11, 51, 35, 279007, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
    ]