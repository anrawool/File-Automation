# Generated by Django 4.2.4 on 2023-08-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default_pic.png', null=True, upload_to='profile_pics'),
        ),
    ]
