from django.contrib import admin
from core.models import Glossary


class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'created_at']
    list_per_page = 20
    list_filter = ['title', 'created_at']


admin.site.register(Glossary, GlossaryAdmin)
