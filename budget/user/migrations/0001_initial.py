# Generated by Django 4.1 on 2023-03-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteam', models.CharField(max_length=20)),
                ('amount', models.IntegerField(max_length=10000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteam', models.CharField(max_length=20)),
                ('amount', models.IntegerField(max_length=10000)),
                ('date', models.DateField()),
            ],
        ),
    ]
