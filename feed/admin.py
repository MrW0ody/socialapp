from django.contrib import admin
from feed.models import Post, Comment


class InlineCommentAdmin(admin.StackedInline):
    model = Comment
    extra = 5


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated', 'active']
    list_filter = ['author', 'created', 'updated', 'active']
    search_fields = ['title', 'content']
    inlines = [InlineCommentAdmin]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'posts', 'created', 'updated']
    list_filter = ['author', 'posts', 'created', 'updated']
    search_fields = ['author', 'content', 'posts']
