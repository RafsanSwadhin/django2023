# Generated by Django 4.2.2 on 2023-06-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=101)),
                ('slug', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('details', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100)),
            ],
        ),
    ]
