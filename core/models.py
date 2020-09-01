import os
from django.utils import timezone
from django.conf import settings
from django.db import models
import pandas as pd
from django.contrib import messages


class ActiveCommonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Glossary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
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
    title = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='content_author')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=0)
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE,
                                 related_name='article_categories', blank=True,
                                 null=True)
    photo = models.FileField(upload_to=get_upload_blog, blank=True)
    tag = models.TextField()
    """
        For seo purpose
    """
    meta_title = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
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
    code = models.IntegerField(blank=True, null=True)

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
    budget = models.BigIntegerField(blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, null=True, related_name='data7')

    def __str__(self):
        return self.source


class ActualExpenditure(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data5', blank=True,
                                      null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='data8', blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    current = models.BigIntegerField(blank=True, null=True)
    capital = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.province_name.name


class TotalBudget(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data3', blank=True,
                                      null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='data1', blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    current = models.BigIntegerField(blank=True, null=True)
    capital = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.province_name.name


class ProvinceBudget(models.Model):
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='data4', blank=True,
                                      null=True)
    office_name = models.CharField(max_length=500, blank=True, null=True)
    actual_expenditure = models.ManyToManyField(ActualExpenditure)
    total_budget = models.ManyToManyField(TotalBudget)

    def __str__(self):
        return self.province_name.name





