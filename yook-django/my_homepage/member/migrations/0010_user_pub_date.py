# Generated by Django 3.2.6 on 2021-09-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_delete_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
