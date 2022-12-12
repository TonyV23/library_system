from django.db import models
from app.models import Borrower, Book

class Borrow(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_starting_date = models.DateField(auto_created=False, auto_now=False)
    borrow_ending_date = models.DateField(auto_created=False, auto_now=False)
