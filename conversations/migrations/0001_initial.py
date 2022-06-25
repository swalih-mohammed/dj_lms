# Generated by Django 3.2.7 on 2022-06-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
            options={
                'ordering': ['order', 'unit', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ConversationCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=True)),
                ('conversation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ConversationCompleted', to='conversations.conversation')),
            ],
        ),
    ]
