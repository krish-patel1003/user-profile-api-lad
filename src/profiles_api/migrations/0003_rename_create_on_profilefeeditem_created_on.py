# Generated by Django 4.1.2 on 2022-10-12 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='create_on',
            new_name='created_on',
        ),
    ]