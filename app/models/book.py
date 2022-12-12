from django.db import models
from app.models import Author, Category

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=30)
    book_language = models.CharField(max_length=10)
    edition_date = models.DateField(auto_created=False, auto_now=False)
    

    def __str__(self) -> str:
        return self.author+ " " +self.category+ " " +self.book_title