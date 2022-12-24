from django.db import models

class Emplacement(models.Model):
    etagere = models.CharField(max_length=10, help_text='etagere')
    rank = models.IntegerField(help_text='rangé du livre')

    def __str__(self) -> str:
        return self.etagere +" "+ self.rank

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['etagere', 'rank'],
                name = 'unique_emplacement'
            )
        ]