from django.forms import ModelForm
from .models import Event

# Create the form class.
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

