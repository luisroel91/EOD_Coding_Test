from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    login_url = 'login'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
