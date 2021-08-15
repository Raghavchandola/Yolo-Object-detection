# Generated by Django 3.0.7 on 2021-07-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_auto_20210721_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='chapter',
        ),
        migrations.AddField(
            model_name='classes',
            name='chapter',
            field=models.ManyToManyField(to='project.Chapters'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='paying',
            field=models.ManyToManyField(default='0', to='project.Course'),
        ),
    ]