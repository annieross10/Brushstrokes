# Generated by Django 3.2.22 on 2023-11-11 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brushstrokes', '0003_alter_artwork_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'verbose_name': 'Artwork', 'verbose_name_plural': 'Artworks'},
        ),
    ]