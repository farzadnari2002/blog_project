# Generated by Django 4.2.7 on 2023-12-21 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0018_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 21, 11, 0, 5, 843719, tzinfo=datetime.timezone.utc)),
        ),
    ]
