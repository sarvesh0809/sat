# Generated by Django 3.1.7 on 2021-04-17 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210415_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filesupload',
            old_name='file',
            new_name='myFile',
        ),
    ]
