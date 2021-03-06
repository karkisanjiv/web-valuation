# Generated by Django 2.1.7 on 2019-04-30 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_measure_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='coordinator',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='invitedco',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='measure',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='outcome',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
        migrations.AddField(
            model_name='rubric',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Department'),
        ),
    ]
