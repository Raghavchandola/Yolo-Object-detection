# Generated by Django 3.1.4 on 2021-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20210523_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('payment_id', models.CharField(max_length=200)),
            ],
        ),
    ]
