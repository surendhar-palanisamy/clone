# Generated by Django 3.1 on 2021-10-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20211019_1403'),
        ('base', '0011_auto_20211019_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]