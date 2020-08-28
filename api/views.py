from rest_framework import viewsets
from django.db.models import Q
from core.models import Glossary, Blog, BlogCategory
from api.serializers.core_serializers import GlossarySerializer, \
    BlogSerializer, BlogCategorySerializer


class GlossaryViewSet(viewsets.ModelViewSet):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer

    def get_queryset(self):
        keywords = self.request.query_params.get('keywords', None)
        if keywords:
            queryset = Glossary.objects.filter(
                Q(title__icontains=keywords) |
                Q(description__icontains=keywords)).order_by('-id')
        else:
            queryset = Glossary.objects.all().order_by('-id')
        return queryset


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
