# Generated by Django 2.2.6 on 2019-10-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Job Title',
                'verbose_name_plural': 'Job Titles',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete='cascade', related_name='employee_city', to='company.City')),
                ('job_title', models.ForeignKey(on_delete='cascade', related_name='employee_job_title', to='company.JobTitle')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employes',
                'index_together': {('first_name', 'last_name')},
            },
        ),
    ]
