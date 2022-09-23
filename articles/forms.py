from django import forms
from .models import Comment, Articles

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={"class":"form-control", 'rows':"5"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={"class":"form-control", 'rows':"3", "placeholder":"Comment"}),
        }