# Generated by Django 4.2.8 on 2023-12-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Armia', '0002_weaponmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnginiryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
            ],
        ),
    ]
