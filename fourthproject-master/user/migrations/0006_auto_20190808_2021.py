# Generated by Django 2.2.4 on 2019-08-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190808_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='username'),
        ),
    ]
