# Generated by Django 4.2.7 on 2024-01-30 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0032_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 30, 21, 18, 55, 545965, tzinfo=datetime.timezone.utc)),
        ),
    ]
