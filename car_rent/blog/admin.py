from django.contrib import admin

from .models import Post, Comment, Contact


@admin.action(description='Published')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Unpublished')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'date_published', 'is_published', 'author_name')
    date_hierarchy = 'date_published'
    list_filter = ('is_published',)
    readonly_fields = ('date_published',)
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'id', 'subtitle', 'author_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_created')
    date_hierarchy = 'date_created'
    readonly_fields = ('name', 'post', 'message', 'date_created')
    search_fields = ('name', 'id')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    date_hierarchy = 'date_created'
    search_fields = ('name', 'id', 'email')
    readonly_fields = ('name', 'email', 'message', 'date_created')
