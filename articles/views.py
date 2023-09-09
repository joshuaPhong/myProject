from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Article


# This view inherits from list view. Is like a select * from article. Get all
# the data from a table
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
