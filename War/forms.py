from django.forms import ModelForm
from .models import Player


# Create the form class.
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'