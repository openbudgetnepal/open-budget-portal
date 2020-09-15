# Generated by Django 3.1 on 2020-09-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='female_population',
        ),
        migrations.RemoveField(
            model_name='province',
            name='male_population',
        ),
        migrations.AddField(
            model_name='province',
            name='female_percentage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='male_percentage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='total_budget',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='total_population',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]