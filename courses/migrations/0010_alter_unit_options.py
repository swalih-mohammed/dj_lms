# Generated by Django 3.2.7 on 2022-01-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20220110_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['course', 'order'], 'verbose_name_plural': 'units'},
        ),
    ]
