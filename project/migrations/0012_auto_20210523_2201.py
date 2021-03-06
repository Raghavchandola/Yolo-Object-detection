# Generated by Django 3.1.4 on 2021-05-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20210523_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='pdf',
            field=models.ManyToManyField(to='project.Pdf'),
        ),
        migrations.AddField(
            model_name='chapters',
            name='vids',
            field=models.ManyToManyField(to='project.Video'),
        ),
        migrations.AlterField(
            model_name='chapters',
            name='notes',
            field=models.ManyToManyField(to='project.Notes'),
        ),
    ]
