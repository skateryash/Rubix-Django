# Generated by Django 5.1.1 on 2024-09-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_affiliates_course_affiliates_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiliates',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='affiliates',
            name='number_of_referral',
        ),
        migrations.RemoveField(
            model_name='affiliates',
            name='user',
        ),
        migrations.AddField(
            model_name='affiliates',
            name='location',
            field=models.CharField(default='India', max_length=50),
        ),
        migrations.AddField(
            model_name='affiliates',
            name='name',
            field=models.CharField(default='Affiliate', max_length=50),
        ),
    ]
