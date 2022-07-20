from django.shortcuts import render, get_object_or_404
from .models import Group, Post
AMOUNT_OF_POSTS = 10


def index(request):
    posts = Post.objects.all()[:AMOUNT_OF_POSTS]
    # Как я понял, здесь нам select_related не понадобится,
    # так как это простой запрос ко всем объектам класса Post.
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.select_related('group')[:AMOUNT_OF_POSTS]
    # А здесь я использовал select_related чтобы интерпретатор не
    # перебирал все посты.
    context = {
        'group': group,
        'posts': posts,
        'title': (f'Записи сообщества {group}'),
    }
    return render(request, 'posts/group_list.html', context)
