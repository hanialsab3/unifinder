# Generated by Django 3.2.13 on 2022-05-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
