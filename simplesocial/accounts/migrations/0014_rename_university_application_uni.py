# Generated by Django 3.2.13 on 2022-05-15 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_application_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='university',
            new_name='uni',
        ),
    ]
