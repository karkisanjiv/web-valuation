# Generated by Django 2.1.1 on 2019-05-02 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_coordinator_last_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='cor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
