# Generated by Django 3.0.14 on 2022-05-09 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HVACtodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='tasks',
        ),
    ]
