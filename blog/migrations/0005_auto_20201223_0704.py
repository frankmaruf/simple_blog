# Generated by Django 3.1.4 on 2020-12-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201222_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Auhor Name'),
        ),
    ]
