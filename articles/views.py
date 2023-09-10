from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


# This view inherits from list view. Is like a select * from article. Get all
# the data from a table
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = (
        'title',
        'body',
        'author',
    )


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = (
        'title',
        'body',
    )


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
