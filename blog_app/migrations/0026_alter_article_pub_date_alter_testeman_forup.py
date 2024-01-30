# Generated by Django 4.2.7 on 2023-12-26 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0025_testeman_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 13, 56, 20, 588978, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='testeman',
            name='forup',
            field=models.BinaryField(null=True),
        ),
    ]
