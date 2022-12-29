from django.forms import ModelForm
from app.models import Emplacement

class EmplacementForm(ModelForm):
    
    class Meta:
        model = Emplacement
        fields = '__all__'