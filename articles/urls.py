from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # Set cache to expire every 24 hours (there are 3600 seconds in an hour)
    # Cache is flushed when an "Article" object is saved.

    path('', cache_page(3600 * 24)(views.ArticleListView.as_view()), name='home'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail_view')

]
