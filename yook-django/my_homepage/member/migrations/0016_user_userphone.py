# Generated by Django 3.2.6 on 2021-09-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_user_useremail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userphone',
            field=models.TextField(blank=True, max_length=128, null=True, verbose_name='전화번호'),
        ),
    ]