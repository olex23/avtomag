# Generated by Django 5.0.4 on 2024-04-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.TextField()),
            ],
        ),
    ]
