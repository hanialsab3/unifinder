# Generated by Django 3.2.13 on 2022-05-22 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_student_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]
