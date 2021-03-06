# Generated by Django 3.2.13 on 2022-05-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_university_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='application',
            new_name='application_debug',
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.CharField(max_length=120)),
                ('cv', models.CharField(max_length=120)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.university')),
            ],
        ),
    ]
