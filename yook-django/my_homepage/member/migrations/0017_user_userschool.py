# Generated by Django 3.2.6 on 2021-09-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0016_user_userphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userschool',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='학교'),
        ),
    ]
