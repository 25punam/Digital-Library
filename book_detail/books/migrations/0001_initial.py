# Generated by Django 5.0.1 on 2024-01-21 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_no', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookmodel')),
            ],
        ),
    ]
