# Generated by Django 5.1.1 on 2024-09-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_affiliates_mode_alter_certificate_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Adavance', 'Adavance')], max_length=100),
        ),
    ]
