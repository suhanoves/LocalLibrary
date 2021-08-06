from catalog.models import *


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'imprint', 'isbn']
    list_filter = ['genres', 'imprint']
    filter_horizontal = ['authors', 'genres']
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Model display
    fieldsets = (
        (None, {
            'fields': ('id', 'book')
        }),
        ('Availability', {
            'fields': ('borrower', 'status', 'due_back')
        }),
    )
    readonly_fields = ['id']

    # List display
    list_display = ['id', 'book', 'borrower', 'status', 'due_back', 'is_overdue']
    list_display_links = ['book']
    list_editable = ['status', 'due_back', 'borrower']
    list_filter = ['status']
    search_fields = ['book__title']

    @admin.display(boolean=True)
    def is_overdue(self, instance):
        return instance.is_overdue


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


class BookInline(admin.TabularInline):
    model = Book.authors.through
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
