# Generated by Django 2.1.1 on 2019-04-06 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190405_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_score',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
    ]
