# Generated by Django 3.1 on 2020-09-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200907_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincebudget',
            name='actual_expenditure',
            field=models.ManyToManyField(help_text='<p style="color:blue;">Please select only one value at a time <p>', to='core.ActualExpenditure'),
        ),
        migrations.AlterField(
            model_name='provincebudget',
            name='total_budget',
            field=models.ManyToManyField(help_text='Please select only one value at a time  ', to='core.TotalBudget'),
        ),
    ]