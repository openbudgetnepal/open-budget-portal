from core.models import Glossary, Blog, BlogCategory
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
