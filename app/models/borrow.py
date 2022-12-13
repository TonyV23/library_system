from django.db import models
from app.models import Borrower, Book
from library_system import settings

class Borrow(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_starting_date = models.DateField(settings.DATE_INPUT_FORMATS,auto_created=False, auto_now=False)
    borrow_ending_date = models.DateField(settings.DATE_INPUT_FORMATS,auto_created=False, auto_now=False)

    def __str__(self) -> str:
        return self.borrower+ " " +self.book