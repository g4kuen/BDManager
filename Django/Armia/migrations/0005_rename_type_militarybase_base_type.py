# Generated by Django 4.2.8 on 2023-12-17 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Armia', '0004_militarybase_alter_enginirytype_name_weapon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='militarybase',
            old_name='type',
            new_name='base_type',
        ),
    ]
