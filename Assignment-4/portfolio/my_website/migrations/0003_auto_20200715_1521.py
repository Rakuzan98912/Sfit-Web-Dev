# Generated by Django 2.2 on 2020-07-15 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0002_auto_20200713_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='fullname',
            new_name='full_name',
        ),
    ]