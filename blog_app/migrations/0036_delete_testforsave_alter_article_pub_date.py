# Generated by Django 4.2.7 on 2024-01-31 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0035_alter_article_pub_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testforsave',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 16, 9, 38, 749696, tzinfo=datetime.timezone.utc)),
        ),
    ]
