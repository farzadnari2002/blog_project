# Generated by Django 4.2.7 on 2023-12-21 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0017_article_pub_date_alter_article_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 21, 10, 58, 23, 217221, tzinfo=datetime.timezone.utc)),
        ),
    ]