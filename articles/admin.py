from django.contrib import admin

from .models import Articles, Comment

class CommentInLine(admin.TabularInline):
    model = Comment

class ArticlesAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment)