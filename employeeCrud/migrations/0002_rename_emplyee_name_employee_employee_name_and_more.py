# Generated by Django 4.2.15 on 2024-08-19 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeCrud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emplyee_name',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emplyee_regNo',
            new_name='employee_regNo',
        ),
    ]
