# Generated by Django 5.0.7 on 2024-07-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchover',
            name='Last_used',
            field=models.DateTimeField(),
        ),
    ]
