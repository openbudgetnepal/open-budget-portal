from django.conf import settings
from django.db import models


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
