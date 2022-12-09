from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(
        max_length=48,
        verbose_name='title'
    )
    subtitle = models.CharField(
        max_length=48,
        verbose_name='subtitle'
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='image'
    )
    text = models.TextField(
        verbose_name='text'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='is published'
    )
    date_published = models.DateTimeField(
        default=now,
        verbose_name='date published'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )
    author_name = models.CharField(
        max_length=96,
        verbose_name='author name',
        default='No information'
    )
    author_about = models.TextField(
        verbose_name='about author',
        default='No information'
    )
    author_image = models.ImageField(
        upload_to='posts/',
        verbose_name='author image',
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('date_published',)


class Comment(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='name'
    )
    message = models.TextField(
        verbose_name='message text'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        verbose_name='post comment'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date comment'
    )

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'blog_comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ('date_created',)


class Contact(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='name'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message = models.TextField(
        verbose_name='contact message'
    )
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date contact'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ('date_created',)
