# Generated by Django 4.1.5 on 2023-01-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_flowerscount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FlowersCount',
            new_name='FollowerCount',
        ),
    ]
