# Generated by Django 4.2.2 on 2023-06-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0004_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='tution/image'),
        ),
    ]