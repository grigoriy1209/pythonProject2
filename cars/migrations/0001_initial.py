# Generated by Django 5.0.7 on 2024-07-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
