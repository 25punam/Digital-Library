# Generated by Django 5.0.1 on 2024-01-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodel',
            name='img',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
