# Generated by Django 4.1.3 on 2023-03-09 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_table_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='row',
            options={},
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['title', '-created']},
        ),
        migrations.RemoveField(
            model_name='table',
            name='date',
        ),
    ]
