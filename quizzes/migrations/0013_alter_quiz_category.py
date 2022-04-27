# Generated by Django 3.2.7 on 2022-04-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0012_auto_20220425_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.CharField(blank=True, choices=[('LISTENING', 'LISTENING'), ('SPEAKING', 'SPEAKING'), ('WRITING', 'WRITING'), ('READING', 'READING'), ('GRAMMAR', 'GRAMMAR'), ('VOCABULARY', 'VOCABULARY'), ('DIALOGUE', 'DIALOGUE'), ('TRANSLATE', 'TRANSLATE'), ('DRAFT EMAIL', 'DRAFT EMAIL'), ('UNIT_TEST', 'UNIT_TEST'), ('REVISION', 'REVISION'), ('GENERAL_ENGLISH', 'GENERAL_ENGLISH'), ('GENERAL_ARABIC', 'GENERAL_ARABIC'), ('OTHER', 'OTHER')], default='OTHER', max_length=250, null=True),
        ),
    ]