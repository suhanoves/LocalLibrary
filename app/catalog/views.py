from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get(self, request, *args, **kwargs):
        # Add a counter of user visits
        visits_count = request.session.get('visits_count', 0)
        request.session['visits_count'] = visits_count + 1

        return super().get(request, *args, **kwargs)


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


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = models.BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 50

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back')
