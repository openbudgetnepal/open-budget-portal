# Generated by Django 3.1 on 2020-09-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_provincebudgetbulk'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='female_population',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='male_population',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='revenue_collected',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='total_budget',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
