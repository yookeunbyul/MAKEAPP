# Generated by Django 3.2.6 on 2021-09-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_alter_user_userbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default='undefine@example.com', max_length=128, verbose_name='이메일'),
            preserve_default=False,
        ),
    ]