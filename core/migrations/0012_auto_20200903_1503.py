# Generated by Django 3.1 on 2020-09-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_province_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]