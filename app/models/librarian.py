from django.db import models

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name+ " "+ self.email