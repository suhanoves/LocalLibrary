from django.contrib import admin

from catalog.models import *


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'imprint', 'isbn']
    list_filter = ['genre', 'imprint']
    filter_horizontal = ['author', 'genre']
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Model display
    fieldsets = (
        (None, {
            'fields': ('id', 'book')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    readonly_fields = ['id']


    # List display
    list_display = ['id', 'book', 'status', 'due_back']
    list_display_links = ['book']
    list_editable = ['status', 'due_back']
    list_filter = ['status']
    search_fields = ['book__title']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


class BookInline(admin.TabularInline):
    model = Book.author.through
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Model display
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # List display
    list_display = ('__str__', 'last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BookInline]


@admin.register(Imprint)
class ImprintAdmin(admin.ModelAdmin):
    pass
