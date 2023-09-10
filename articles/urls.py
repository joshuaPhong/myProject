from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(),
         name='article_detail'),
    path('article_create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(),
         name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(),
         name='article_delete'),
]
