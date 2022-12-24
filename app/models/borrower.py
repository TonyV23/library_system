from django.db import models
from phone_field import PhoneField


class Borrower(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    nationality = models.CharField(max_length=20)
    phone = PhoneField(blank =True)
    email = models.EmailField()


    def __str__(self) -> str:
        return self.first_name+ " " +self.last_name

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name','gender', 'nationality', 'phone', 'email'],
                name = 'unique_borrower'
            )
        ]