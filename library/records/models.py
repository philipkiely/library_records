from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=150)
    published = models.DateField()
    isbn = models.IntegerField(unique=True)

    def __str__(self):
        return self.title + " by " + self.author

class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.user.username

class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    out_to = models.ForeignKey(Patron, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        has_copy = "checked in"
        if self.out_to:
            has_copy = self.out_to.user.username
        return self.book.title + " -> " + has_copy