from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Group, Post, User
AMOUNT_OF_POSTS = 10
AMOUNT_SYMBOLS_TITLE = 30


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, AMOUNT_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related('group')
    paginator = Paginator(post_list, AMOUNT_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
        'title': (f'Записи сообщества {group}'),
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    author_post_list = author.posts.select_related('author')
    paginator = Paginator(author_post_list, AMOUNT_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_count = author_post_list.count()
    if author.get_full_name():
        author = author.get_full_name()
    context = {
        'author': author,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author.get_full_name():
        author = post.author.get_full_name()
    else:
        author = post.author
    author_post_count = post.author.posts.select_related('author').count()
    context = {
        'author': author,
        'post': post,
        'title': (f'Пост  {post.text[:AMOUNT_SYMBOLS_TITLE]}'),
        'author_post_count': author_post_count,
    }
    return render(request, 'posts/post_detail.html', context)
