from django.forms import ModelForm
from app.models import Borrower

class BorrowerForm(ModelForm):
    
    class Meta:
        model = Borrower
        fields = '__all__'