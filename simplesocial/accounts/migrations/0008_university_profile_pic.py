# Generated by Django 3.2.13 on 2022-05-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220505_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='universities'),
        ),
    ]
