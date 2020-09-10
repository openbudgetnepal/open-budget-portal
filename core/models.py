import os
from django.utils import timezone
from django.conf import settings
from django.db import models
import pandas as pd
from django.contrib import messages
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


class ActiveCommonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Glossary(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="glossary_admin")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="glossary")
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    objects = ActiveCommonManager()
    all_objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        get_latest_by = ['-created_at']


def get_upload_blog(instance, filename):
    return os.path.join("Content", instance.title, filename)


class BlogCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Publish'),
        (2, 'UnPublish'),
    )
    title = RichTextField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='content_author')
    content = RichTextField()
    publish = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=0,help_text='Only Numeric Value Without Comma')
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE,
                                 related_name='article_categories', blank=True,
                                 null=True)
    photo = models.FileField(upload_to=get_upload_blog, blank=True)
    tag = RichTextField()
    """
        For seo purpose
    """
    meta_title = RichTextField(null=True, blank=True)
    meta_keywords = RichTextField(null=True, blank=True)
    meta_description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="blog_admin")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="blogs")
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)


class Information(models.Model):
    TYPE_CHOICES = (('mission', 'Our Mission'),
                    ('about', 'About Us'),
                    ('connect', 'Connect with Us'),
                    ('terms', 'Terms & Condition'),
                    ('privacy', 'Privacy'))
    info_type = models.CharField(max_length=75, choices=TYPE_CHOICES,
                                 unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="information_admin")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   db_index=True,
                                   editable=False, on_delete=models.SET_NULL,
                                   related_name="information")
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)


class Province(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=True, null=True)
    image = models.FileField(upload_to='pics', blank=True, null=True)
    code = models.IntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    total_budget = models.CharField(max_length=200, blank=True, null=True)
    male_percentage = models.CharField(max_length=200, blank=True, null=True)
    female_percentage = models.CharField(max_length=200, blank=True, null=True)
    total_population = models.CharField(max_length=200, blank=True, null=True)
    male_percentage = models.CharField(max_length=200, blank=True, null=True)
    economic_growth = models.CharField(max_length=100, blank=True, null=True)
    share_in_domestic_product = models.CharField(max_length=100, blank=True, null=True)
    human_development_index = models.CharField(max_length=100, blank=True, null=True)
    multidimensional_poverty_index = models.CharField(max_length=100, blank=True, null=True)
    total_gross_domestic_product = models.CharField(max_length=100, blank=True, null=True)
    per_capital_income = models.CharField(max_length=100,blank=True, null=True)
    revenue_collected = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.year


class ProvinceSource(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data6', blank=True,
                                      null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, null=True, related_name='data7',
                             help_text='Please select a recent year... ')

    def __str__(self):
        return self.source


class ActualExpenditure(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data5', blank=True,
                                      null=True)
    office_name = models.CharField(max_length=500, blank=True, null=True)

    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='data8', blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    current = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    capital = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')

    def __str__(self):
        return self.province_name.name + ' ' + self.office_name + ' ' + str(self.year.year)


class TotalBudget(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data3', blank=True,
                                      null=True)
    office_name = models.CharField(max_length=500, blank=True, null=True)

    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='data1', blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    current = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')
    capital = models.BigIntegerField(blank=True, null=True,help_text='Only Numeric Value Without Comma')

    def __str__(self):
        return self.province_name.name + ' ' + self.office_name + ' ' + str(self.year.year)


class ProvinceBudget(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data4', blank=True,
                                      null=True)
    office_name = models.CharField(max_length=500, blank=True, null=True)
    actual_expenditure = models.ManyToManyField(ActualExpenditure,
                                                help_text='<p style="color:blue;font-size:25px;">Please select only one value at a time <p>')
    total_budget = models.ManyToManyField(TotalBudget,
                                          help_text='<p style="color:blue;font-size:25px;">Please select only one value at a time <p>')

    def __str__(self):
        return self.province_name.name + ' ' + self.office_name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    message = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


class AboutMission(models.Model):
    missions = RichTextField(blank=True, null=True)


class ExtraNecessaryData(models.Model):
    overallpopulation = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and ExtraNecessaryData.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one ExtraNecessaryDAta instance')
        return super(ExtraNecessaryData, self).save(*args, **kwargs)



