# Generated by Django 2.2.5 on 2021-02-06 14:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jiranapp', '0014_auto_20190930_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
