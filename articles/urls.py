from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
)

urlpatterns = [
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('', ArticleListView.as_view(), name='article_list'),
]