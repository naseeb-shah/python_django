# Generated by Django 5.0.1 on 2024-02-04 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='data',
        ),
    ]
