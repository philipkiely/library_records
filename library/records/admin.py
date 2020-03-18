from django.contrib import admin
from .models import Book, Patron, Copy

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published")

class PatronAdmin(admin.ModelAdmin):
    pass

class CopyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Copy, CopyAdmin)
