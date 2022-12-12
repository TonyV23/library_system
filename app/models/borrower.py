from django.db import models


class Borrower(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    nationality = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.first_name+ " " +self.last_name