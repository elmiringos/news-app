from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from articles.models import Articles
from django import forms

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user_profile.html'
    success_url = reverse_lazy('home')
    form_class = CustomUserChangeForm

    password = forms.CharField(label='', widget=forms.PasswordInput, help_text='Minimum 8 characters.')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
       context = super(ProfileView, self).get_context_data(**kwargs)
       context['article_list'] = Articles.objects.all()
       return context