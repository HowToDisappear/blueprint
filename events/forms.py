from django import forms
from .models import LOC_CHOICES, ETYPE_CHOICES

LOC_CHOICES.insert(0, ('all', 'All locations'))

WHEN_CHOICES = [
    ('at', 'All time'),
    ('tw', 'This week'),
    ('nw', 'Next week'),
    ('tm', 'This month'),
    ('nm', 'Next month'),
]

class FilterForm(forms.Form):
    etype = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ETYPE_CHOICES,
        label="Event type",
    )
    location = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=LOC_CHOICES,
    )
    when = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=WHEN_CHOICES,
    )