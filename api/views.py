from rest_framework import viewsets
from django.db.models import Q
from core.models import Glossary, Blog, BlogCategory, Information, Province, ProvinceSource, ProvinceBudget
from api.serializers.core_serializers import GlossarySerializer, \
    BlogSerializer, BlogCategorySerializer, InformationSerializer, \
    ProvinceSerializer, ProvinceSourceSerializer, ProvinceBudgetSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated


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


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class ProvinceSourceViewSet(viewsets.ModelViewSet):
    queryset = ProvinceSource.objects.all()
    serializer_class = ProvinceSourceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'province_name__code', 'source', 'budget', 'year']

    def get_queryset(self):
        queryset = ProvinceSource.objects.order_by('id')
        return queryset

    def get_serializer_class(self):
        serializer_class = ProvinceSourceSerializer
        return serializer_class


class ProvinceBudgetViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ProvinceBudget.objects.all()
    serializer_class = ProvinceBudgetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'office_name', 'province_name__code', 'actual_expenditure', 'total_budget']

    def get_queryset(self):
        queryset = ProvinceBudget.objects.order_by('id')
        return queryset


