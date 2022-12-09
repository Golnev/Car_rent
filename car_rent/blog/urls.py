from django.urls import path

from .views import PostListView, PostDetailView, ContactCreateView, AboutTemplateView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about')
]
