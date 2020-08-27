from core.models import Glossary
from rest_framework import serializers


class GlossarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Glossary
        fields = ['id', 'title', 'description']
