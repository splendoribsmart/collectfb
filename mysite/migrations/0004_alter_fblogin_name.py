# Generated by Django 4.0.1 on 2022-04-21 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_fblogin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fblogin',
            name='name',
            field=models.CharField(default='home boy', max_length=120),
        ),
    ]
