# Generated by Django 5.0.1 on 2024-02-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='details',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
