from django.forms import ModelForm
from app.models import Book

class BookForm(ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
