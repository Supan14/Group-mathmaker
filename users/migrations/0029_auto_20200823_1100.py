# Generated by Django 3.1 on 2020-08-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(1, 'male'), (1, 'female')], max_length=50, null=True),
        ),
    ]
