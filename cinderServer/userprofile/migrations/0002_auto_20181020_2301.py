# Generated by Django 2.1.2 on 2018-10-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='John Doe', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default='none', max_length=100),
        ),
    ]