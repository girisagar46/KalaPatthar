from django.urls import path
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('crawl/', views.CrawlSites.as_view(), name='crawl_sites'),
]