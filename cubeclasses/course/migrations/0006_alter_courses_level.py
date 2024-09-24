# Generated by Django 5.1.1 on 2024-09-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_courses_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='level',
            field=models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCE', 'Advance')], max_length=100),
        ),
    ]
