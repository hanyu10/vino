from django import forms
from wine.models import Wine

class SearchForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('name', 'wine_type', 'sugar', 'sour', 'area')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'wine_type': forms.TextInput(attrs={'class': 'form-control'}),
            'sugar': forms.NumberInput(attrs={'class': 'form-control'}),
            'sour': forms.NumberInput(attrs={'class': 'form-control'}),
        }
