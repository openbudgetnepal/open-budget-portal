from django.urls import include, path
from api.views import GlossaryViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'glossary-api', GlossaryViewSet)

urlpatterns = router.urls
