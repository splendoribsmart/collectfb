# Generated by Django 4.0.1 on 2022-04-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_newlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fblogin',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]