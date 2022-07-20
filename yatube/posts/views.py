from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:10]
    # Так и не сообразил, как тут можно сделать изящнее.
    # И вот это '.all()[:10]' меня смущает.
    # Сначала берем всё, а потом из него только 10 первых.
    # Попытался сделать .range(10), но интерпретатор ругается.
    # В Meta class тоже такого среза не нашел.
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': (f'Записи сообщества {group}'),
    }
    return render(request, 'posts/group_list.html', context)
