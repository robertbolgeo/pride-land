# Generated by Django 5.1 on 2024-09-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_alter_volunteer_restrictions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='status',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_accepted',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
