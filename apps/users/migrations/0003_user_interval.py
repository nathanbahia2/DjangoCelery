# Generated by Django 3.2.9 on 2021-12-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interval',
            field=models.CharField(default='1', max_length=3),
        ),
    ]
