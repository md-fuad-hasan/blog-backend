# Generated by Django 4.2.3 on 2023-07-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_accountdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountdetail',
            old_name='propfile_pic',
            new_name='profile_pic',
        ),
    ]
