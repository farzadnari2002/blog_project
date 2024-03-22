# Generated by Django 4.2.7 on 2024-03-22 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0048_socialmedia_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'شبکه اجتماعی', 'verbose_name_plural': 'شبکه های اجتماعی'},
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 10, 20, 58, 759798, tzinfo=datetime.timezone.utc), verbose_name='تاریخ نشر'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='instagram',
            field=models.URLField(verbose_name='اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='telegram',
            field=models.URLField(verbose_name='تلگرام'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='whatsapp',
            field=models.URLField(verbose_name='واتساپ'),
        ),
    ]