# Generated by Django 3.2.7 on 2021-10-13 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211013_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorites',
            old_name='owner',
            new_name='user',
        ),
    ]
