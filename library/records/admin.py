from django.contrib import admin
from .models import Book, Patron, Copy

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published")
    actions = ["make_copys"]

    def make_copys(self, request, queryset):
        for q in queryset:
            q.make_copy()
        self.message_user(request, "copy(s) created")
    make_copys.short_description = "Add a copy of book(s)"

class CopyAdmin(admin.ModelAdmin):
    actions = ["check_in_copys"]

    def check_in_copys(self, request, queryset):
        for q in queryset:
            q.check_in()
        self.message_user(request, "copy(s) checked in")
    check_in_copys.short_description = "Check in copy(s)"

admin.site.register(Book, BookAdmin)
admin.site.register(Copy, CopyAdmin)
admin.site.register(Patron)
