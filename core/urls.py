from django.urls import path, include
from .views import BudgetVisualization, HomePage,Blog
from . import views

urlpatterns = [

    path('budgetvisualization/<int:pk>', BudgetVisualization.as_view(), name='budgetvisualization'),
    path('blog', Blog.as_view(), name='blog'),
    path('', HomePage.as_view(), name='index'),
    path('contact', views.contact, name='contact')

]
