from django.urls import include, path
from api.views import GlossaryViewSet, BlogViewSet, BlogCategoryViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'glossary-api', GlossaryViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'blog-category', BlogCategoryViewSet)

urlpatterns = router.urls
