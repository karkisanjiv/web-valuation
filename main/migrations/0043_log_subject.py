# Generated by Django 2.1.1 on 2019-05-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_outcome_status_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='subject',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
