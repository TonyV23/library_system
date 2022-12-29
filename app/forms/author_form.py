from django.forms import ModelForm
from app.models import Author

class AuthorForm(ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'