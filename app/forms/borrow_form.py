from django.forms import ModelForm
from app.models import Borrow

class BorrowForm(ModelForm):
    
    class Meta:
        model = Borrow
        fields = '__all__'