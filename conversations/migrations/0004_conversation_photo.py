# Generated by Django 3.2.7 on 2022-04-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20220205_0648'),
        ('conversations', '0003_conversationcompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='assets.photo'),
        ),
    ]