from django.contrib import admin
from core.models import Glossary, Year, Province, ProvinceSource, TotalBudget, ActualExpenditure, ProvinceBudget, \
    Contact, Blog, AboutMission ,ExtraNecessaryData
from import_export.admin import ImportExportModelAdmin


class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'created_at']
    list_per_page = 20
    list_filter = ['title', 'created_at']


admin.site.register(Year)


class ProvinceAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Province, ProvinceAdmin)

admin.site.register(AboutMission)



class ProvinceSourceAdmin(ImportExportModelAdmin):
    pass
admin.site.register(ProvinceSource, ProvinceSourceAdmin)

class TotalBudgetAdmin(ImportExportModelAdmin):
    pass
admin.site.register(TotalBudget,TotalBudgetAdmin)

class ActualExpenditureAdmin(ImportExportModelAdmin):
    pass
admin.site.register(ActualExpenditure,ActualExpenditureAdmin)


class ProvinceBudgetAdmin(ImportExportModelAdmin):
    pass
admin.site.register(ProvinceBudget, ProvinceBudgetAdmin)

class GlossaryAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Glossary, GlossaryAdmin)


admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(ExtraNecessaryData)