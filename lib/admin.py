from django.contrib import admin
from .models import *
admin.site.register(Genre)
#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last', 'first', 'year',)
    list_filter = ('last', 'year')

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genres_str',)

admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'status', 'due_back',)
    list_filter = ('status',)

admin.site.register(BookInstance, BookInstanceAdmin)
# Register your models here.
