from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractModel):
    pass


class Genre(AbstractModel):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class Book(AbstractModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    description = models.TextField(verbose_name='Описание')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='books')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    price = models.FloatField(verbose_name='Цена', default=0.0)
    users = models.ManyToManyField(User, related_name='favorites')

    def __str__(self):
        return f'{self.name} [{self.author if self.author else "Не выбран"}]'

    class Meta:
        ordering = ['-date_created']


class Author(AbstractModel):
    AGES_CHOICE = (('male', 'Мужчина'), ('female', 'Женщина'))
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    sex = models.CharField(choices=AGES_CHOICE, max_length=10, verbose_name='Пол')
    author_image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-date_created']
