# Generated by Django 4.2.11 on 2024-04-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_rename_step_numer_instructions_step_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='picture',
            new_name='cuisine',
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]