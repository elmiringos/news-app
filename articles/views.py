from django.http import request
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Articles, Comment
from .forms import CommentForm, ArticleForm


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticleForm
    template_name = 'article_create.html'
    login_url = 'login'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'
    login_url = 'login'
    context_object_name = 'article_list'

class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'article'
    template_name = 'article_detail.html'
    login_url = 'login'
    
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    form_class = ArticleForm
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse('article_detail', kwargs={'pk': article.pk}) + '#comments'

