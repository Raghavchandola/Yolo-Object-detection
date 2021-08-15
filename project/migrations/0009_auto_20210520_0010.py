# Generated by Django 3.1.4 on 2021-05-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20210517_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
                ('chapter_description', models.TextField(max_length=300)),
                ('chapter_image', models.ImageField(upload_to='myfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='classes',
            name='class_subj',
        ),
        migrations.AddField(
            model_name='classes',
            name='class_subj',
            field=models.ManyToManyField(to='project.Subjects'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='chapter',
            field=models.ManyToManyField(to='project.Chapters'),
        ),
    ]
