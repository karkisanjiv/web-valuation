# Generated by Django 2.1.1 on 2019-04-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_custom_students_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]