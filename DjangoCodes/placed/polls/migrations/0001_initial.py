# Generated by Django 4.1.2 on 2023-11-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Internship', models.CharField(max_length=100)),
                ('CGPA', models.CharField(max_length=100)),
                ('Hostel', models.CharField(max_length=100)),
                ('HistoryOfBacklogs', models.CharField(max_length=100)),
            ],
        ),
    ]