from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.
class ArticleList(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/articles.html"
    paginate_by = 5

class ArticleDetails(DetailView):
    model = Article
    template_name = "blog/article_details.html"