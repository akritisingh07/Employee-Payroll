# Generated by Django 5.0.6 on 2024-07-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_registration_db_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
