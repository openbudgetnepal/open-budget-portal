from django.urls import include, path
from api.views import GlossaryViewSet, BlogViewSet, BlogCategoryViewSet, \
    InformationViewSet, ProvinceViewSet, ProvinceSourceViewSet
from api import views

urlpatterns = [
    path('glossary-api', views.GlossaryViewSet.as_view({'get': 'list'}), name='glossary'),
    path('blog', views.BlogViewSet.as_view({'get': 'list'}), name='blog'),
    path('blog-category', views.BlogCategoryViewSet.as_view({'get': 'list'}), name='blog-category'),
    path('information-api', views.InformationViewSet.as_view({'get': 'list'}), name='information'),
    path('province', views.ProvinceViewSet.as_view({'get': 'list'}), name='province'),
    path('province-source', views.ProvinceSourceViewSet.as_view({'get': 'list'}), name='province-source'),
    path('province-budget', views.ProvinceBudgetViewSet.as_view({'get': 'list'}), name='province-source'),

]
