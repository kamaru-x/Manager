# Generated by Django 5.0.8 on 2024-11-22 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='journal',
            new_name='content',
        ),
    ]