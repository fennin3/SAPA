# Generated by Django 3.1.7 on 2021-05-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_is_subadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='subadminpermission',
            name='can_read_incident',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subadminpermission',
            name='can_reply_messages',
            field=models.BooleanField(default=True),
        ),
    ]
