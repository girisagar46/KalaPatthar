from django.urls import path
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('crawl/', views.CrawlSites.as_view(), name='crawl_sites'),
    path('view_all/', views.ScrappedSitesView.as_view(), name='view_all'),
    path('detail/<str:id>', views.web_detail, name='detail'),
]