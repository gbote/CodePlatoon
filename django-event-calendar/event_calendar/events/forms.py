from django import forms
from .models import *


class EventForm(forms.ModelForm):

  class Meta:
    model = Event
    fields = "__all__"
    widgets = { 
    "starts_at" : forms.DateInput(), 
    "ends_at": forms.DateInput() ,
    'description': forms.Textarea(attrs={'rows': 2})}

