# Generated by Django 3.1.4 on 2021-05-17 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210517_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classes',
            old_name='class_name',
            new_name='classes_name',
        ),
        migrations.RenameField(
            model_name='subjects1',
            old_name='class_subj',
            new_name='class_name',
        ),
    ]
