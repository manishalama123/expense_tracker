from django import forms
from .models import Tracker

class TrackerForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('rent', 'Rent'),
        ('other', 'Other'),
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)  # Dropdown field

    class Meta:
        model = Tracker
        fields = ['amount', 'category', 'description', 'receipts']
