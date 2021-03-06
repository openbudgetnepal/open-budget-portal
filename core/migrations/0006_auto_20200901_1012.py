# Generated by Django 3.1 on 2020-09-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200901_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='female_population',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='male_population',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='per_capital_income',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='revenue_collected',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='total_budget',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='total_population',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
