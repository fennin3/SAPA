# Generated by Django 3.1.7 on 2021-04-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constituent_operations', '0006_actionplantoassemblyman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='message',
            field=models.CharField(max_length=10000),
        ),
    ]
