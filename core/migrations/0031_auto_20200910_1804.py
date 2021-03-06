# Generated by Django 3.1 on 2020-09-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_delete_juicerbasesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualexpenditure',
            name='capital',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='actualexpenditure',
            name='current',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='actualexpenditure',
            name='total',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'UnPublish')], default=0, help_text='Only Numeric Value Without Comma'),
        ),
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.IntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='per_capital_income',
            field=models.CharField(blank=True, help_text='Only Numeric Value Without Comma', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='provincesource',
            name='budget',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='totalbudget',
            name='capital',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='totalbudget',
            name='current',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
        migrations.AlterField(
            model_name='totalbudget',
            name='total',
            field=models.BigIntegerField(blank=True, help_text='Only Numeric Value Without Comma', null=True),
        ),
    ]
