# Generated by Django 3.1.7 on 2021-04-09 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constituent_operations', '0009_problemsforactionplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionplantoassemblyman',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
