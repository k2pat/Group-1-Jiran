# Generated by Django 2.2.5 on 2021-02-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiranapp', '0014_auto_20190930_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
