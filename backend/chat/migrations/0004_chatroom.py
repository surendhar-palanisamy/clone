# Generated by Django 3.2.8 on 2021-11-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatmessage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_1', models.CharField(blank=True, default='1', max_length=100)),
                ('user_id_2', models.CharField(blank=True, default='2', max_length=100)),
                ('room_name', models.CharField(blank=True, default='cool', max_length=100)),
            ],
        ),
    ]
