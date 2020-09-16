# Generated by Django 3.1 on 2020-09-16 11:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20200915_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='list_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='list_title',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
