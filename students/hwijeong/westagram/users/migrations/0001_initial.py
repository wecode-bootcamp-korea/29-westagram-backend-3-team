# Generated by Django 4.0.1 on 2022-01-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]