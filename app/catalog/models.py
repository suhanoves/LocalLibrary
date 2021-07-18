import uuid

from django.db import models
from django.urls import reverse


class Book(models.Model):
    """
    Класс представляющий информацию о книге (не о конкретном экземпляре)
    """
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(
        'Author',
        related_name="books",
        related_query_name="book",
    )
    summary = models.TextField(
        max_length=2500,
        help_text="Введите описание книги"
    )
    imprint = models.ForeignKey('Imprint', on_delete=models.CASCADE)
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>'
    )
    genres = models.ManyToManyField(
        'Genre',
        related_name="books",
        related_query_name="book",
        help_text='Выберите жанры, подходящие для этой книги',
    )
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class BookInstance(models.Model):
    """
    Модель, представляющая конкретный экземпляр книги
    имеиющийся в нашей библиотеке и который можно взять
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Уникальный идентификатор для этой конкретной книги во всей библиотеке"
    )
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name="instances",
        related_query_name="instance",
    )
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Тех.обслуживание'),
        ('o', 'Арендована'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='m',
        help_text='Доступность книги'
    )

    def __str__(self):
        return f'{self.id} {self.book.title}'

    class Meta:
        ordering = ['due_back']
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


class Genre(models.Model):
    """
    Модель претсавляющая жанры книг (Научная фантастика, Проза)
    """
    name = models.CharField(
        verbose_name='Тип',
        max_length=200,
        help_text='Укажите жанр книги: Фантастика, Французская поэзия и.т.д'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Language(models.Model):
    """
    Модель, представляющая основной язык книги
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Author(models.Model):
    """
    Модель, представляющая автора
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('catalog:author', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Imprint(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
