# Generated by Django 3.2.6 on 2021-09-24 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_alter_member_memberbirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='memberbirth',
        ),
    ]
