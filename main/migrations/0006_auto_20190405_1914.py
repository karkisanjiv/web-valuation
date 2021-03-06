# Generated by Django 2.1.1 on 2019-04-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190404_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='cutoff_type',
            field=models.CharField(choices=[('Percentage', 'Percentage'), ('Percentile', 'Percentile'), ('Average', 'Average')], default='Percentage', max_length=100),
        ),
        migrations.AddField(
            model_name='measure',
            name='tool_type',
            field=models.CharField(choices=[('Rubric', 'Rubric'), ('Test score', 'Test score')], default='Rubric', max_length=100),
        ),
    ]
