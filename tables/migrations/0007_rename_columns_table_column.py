# Generated by Django 4.1.3 on 2023-01-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_remove_column_table_table_columns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='columns',
            new_name='column',
        ),
    ]
