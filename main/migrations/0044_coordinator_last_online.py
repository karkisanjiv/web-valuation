# Generated by Django 2.1.1 on 2019-05-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_log_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='last_online',
            field=models.DateTimeField(null=True),
        ),
    ]
