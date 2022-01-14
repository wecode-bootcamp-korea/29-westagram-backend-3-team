# Generated by Django 4.0.1 on 2022-01-14 07:59

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True, validators=[users.validators.isEmailValid, users.validators.checkEmailAndPassword])),
                ('password', models.CharField(max_length=200, validators=[users.validators.isPasswordValid, users.validators.checkEmailAndPassword])),
                ('contact', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
