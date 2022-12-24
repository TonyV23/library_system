from django.db import models
from app.models import Author, Category, Emplacement


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=30)
    exemplaire = models.IntegerField()
    book_language = models.CharField(max_length=10)
    edition_date = models.DateField()
    

    def __str__(self) -> str:
        return self.book_title

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['book_title', 'exemplaire','book_language', 'edition_date'],
                name = 'unique_book'
            )
        ]