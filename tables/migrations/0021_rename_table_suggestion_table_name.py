# Generated by Django 4.1.3 on 2023-03-17 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0020_suggestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='table',
            new_name='table_name',
        ),
    ]
