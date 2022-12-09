from django.http import HttpRequest
from django.views.generic import ListView, DetailView, TemplateView

from .models import Post, Comment
from .forms import CommentForm, ContactForm


class ContextMixin:
    context = {
        'site_title': ('car', 'book'),
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'instagram': 'https://www.instagram.com/',
        'address': 'Belarus, Minsk',
        'phone': '+375 29 111 11 11',
        'mail': 'email@gmail.com'
    }


class PostListView(ContextMixin, ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context


class PostDetailView(ContextMixin, DetailView):
    model = Post
    template_name = 'blog/blog-single.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context.update(self.context)
        context['comment'] = Comment.objects.filter(post__id=context[self.context_object_name].id)
        context['comment_form'] = CommentForm()
        context['user'] = self.request.user
        return context

    def post(self, request: HttpRequest, post_slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request, post_slug=post_slug)


class ContactCreateView(ContextMixin, TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data()
        context.update(self.context)
        context['contact_form'] = ContactForm()
        context['user'] = self.request.user
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context.update(self.context)
        return context
