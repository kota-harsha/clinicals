# Generated by Django 5.0.6 on 2024-10-31 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('data_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('clinic_history', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('medical_history', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(choices=[('hw', 'Height / Weight'), ('bp', 'Blood Pressure'), ('hr', 'Heart Rate')], max_length=20)),
                ('componentValue', models.CharField(max_length=20)),
                ('measuredDataTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalsApp.patient')),
            ],
        ),
    ]
