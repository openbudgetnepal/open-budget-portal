# Generated by Django 3.1 on 2020-09-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_delete_aboutpartner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincesource',
            name='budget',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
