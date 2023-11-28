from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", "is_bestselling")
    list_display = ("title", "author", "rating", "is_bestselling")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
