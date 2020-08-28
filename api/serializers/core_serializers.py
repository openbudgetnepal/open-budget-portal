from core.models import Glossary, Blog, BlogCategory, Information, Province
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
