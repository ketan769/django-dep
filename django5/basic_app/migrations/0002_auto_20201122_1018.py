# Generated by Django 3.1.2 on 2020-11-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfolio_site',
            new_name='profile_site',
        ),
    ]
