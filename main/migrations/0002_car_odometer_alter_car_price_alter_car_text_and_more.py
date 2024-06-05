# Generated by Django 5.0.4 on 2024-04-25 13:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='odometer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]