# Generated by Django 2.1.1 on 2019-04-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_category_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_students',
            name='current',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
