from django.urls import path, include
from .views import BudgetVisualization, HomePage, BlogData, BlogDetailView, AboutView, GlossaryView
from . import views

urlpatterns = [

    path('budgetvisualization/<int:pk>', BudgetVisualization.as_view(), name='budgetvisualization'),
    path('blog', BlogData.as_view(), name='blog'),
    path('', HomePage.as_view(), name='index'),
    path('contact', views.contact, name='contact'),
    path('blogdetail/<int:pk>', BlogDetailView.as_view(), name='blogdetail'),
    path('about', AboutView.as_view(), name='about'),
    path('glossary', GlossaryView.as_view(), name='glossary')

]
