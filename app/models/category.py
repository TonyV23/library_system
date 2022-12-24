from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.category_name

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['category_name'],
                name = 'unique_category'
            )
        ]