from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, BookAuthor

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
# Register your models here.

class BookAuthorInlineForBook(admin.TabularInline):
    """show / edit the BookAuthor rows when editing a Book."""
    model = BookAuthor
    extra = 1


class BookAuthorInlineForAuthor(admin.TabularInline):
    """show / edit the BookAuthor rows when editing an Author."""
    model = BookAuthor
    fk_name = 'author'          # explicit because we’ll reuse the inline
    extra = 1

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAuthorInlineForAuthor]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre')
    inlines = [BooksInstanceInline, BookAuthorInlineForBook]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
