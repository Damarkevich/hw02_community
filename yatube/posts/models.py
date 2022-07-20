from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='group_posts',
        # Ниже в модели authors у меня тоже было related_name='posts'
        # Понимаю, что даже если они будут одинаковые,
        # тоже всё будет работать.
        # Но мне показалось, что так не красиво.
        # Если так не принято - с удовольствием исправлю.
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_posts',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Posts'
