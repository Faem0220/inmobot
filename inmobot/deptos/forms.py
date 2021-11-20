from django import forms

class Seleccionados(forms.Form):
    selected = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )
