from core.models import Glossary, Blog, BlogCategory, Information, Province, ProvinceSource, ProvinceBudget
from rest_framework import serializers


class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Glossary
        fields = ['id', 'title', 'description']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class ProvinceSourceSerializer(serializers.ModelSerializer):
    province_name = serializers.SerializerMethodField()
    province_code = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = ProvinceSource
        fields = '__all__'

    def get_province_name(self, obj):
        name = obj.province_name.name
        return name

    def get_province_code(self, obj):
        code = obj.province_name.code
        return code

    def get_year(self, obj):
        year = obj.year.year
        return year


class ProvinceBudgetSerializer(serializers.ModelSerializer):
    province_name = serializers.SerializerMethodField()
    province_code = serializers.SerializerMethodField()
    actual_expenditure = serializers.SerializerMethodField()
    total_budget = serializers.SerializerMethodField()

    class Meta:
        model = ProvinceBudget
        fields = ['id', 'province_name', 'province_code', 'office_name', 'actual_expenditure', 'total_budget']

    def get_province_name(self, obj):
        name = obj.province_name.name
        return name

    def get_province_code(self, obj):
        code = obj.province_name.code
        return code

    def get_actual_expenditure(self, obj):
        data = []
        qs = obj.actual_expenditure.all().values('year__year', 'total', 'current', 'capital')
        for q in qs:
            data.append(
                {
                    'year': q['year__year'],
                    'total': q['total'],
                    'current': q['current'],
                    'capital': q['capital']
                }

            )
        return data

    def get_total_budget(self, obj):
        data = []
        qs = obj.actual_expenditure.all().values('year__year', 'total', 'current', 'capital')
        for q in qs:
            data.append(
                {
                    'year': q['year__year'],
                    'total': q['total'],
                    'current': q['current'],
                    'capital': q['capital']
                }

            )
        return data
