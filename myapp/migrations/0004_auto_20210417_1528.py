# Generated by Django 3.1.7 on 2021-04-17 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210417_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filesupload',
            old_name='myFile',
            new_name='file',
        ),
    ]
