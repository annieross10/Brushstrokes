# Generated by Django 3.2.22 on 2023-11-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brushstrokes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='excerpt',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]
