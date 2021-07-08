# django
from django.views.generic import ListView
# local
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
