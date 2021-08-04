from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from catalog import models


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        # Заголовок страницы
        context['title'] = 'Главная страница'

        # Статистика библиотеки
        num_authors = models.Author.objects.count()
        num_books = models.Book.objects.count()
        num_instances = models.BookInstance.objects.count()

        # Доступные книги (статус = 'a')
        num_instances_available = models.BookInstance.objects.filter(status='a').count()

        extra_context = {
            'num_books': num_books, 'num_instances': num_instances,
            'num_instances_available': num_instances_available, 'num_authors': num_authors
        }

        context.update(extra_context)
        return context


class BooksView(ListView):
    model = models.Book
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список книг'
        return context


class BookView(DetailView):
    model = models.Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class AuthorsView(ListView):
    model = models.Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список авторов'
        return context


class AuthorView(DetailView):
    model = models.Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object
        return context
