# Generated by Django 4.2.8 on 2023-12-17 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Armia', '0005_rename_type_militarybase_base_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='militarybase',
            old_name='location',
            new_name='id',
        ),
    ]