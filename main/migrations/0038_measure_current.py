# Generated by Django 2.1.1 on 2019-04-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
