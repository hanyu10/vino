from django import forms
from wine.models import Wine

# 동적으로 하는 방법?
TYPE_CHOICES = [
    ('','-'),
    ('White', 'White'),
    ('Rose', 'Rose'),
    ('Sparkling', 'Sparkling'),
    ('Red', 'Red'),
    ('Fortified', 'Fortified'),
]

FOOD_CHOICES = [
    ('','-'),
    ('Beef','Beef'),
    ('Fish','Fish'),
    ('Chicken','Chicken'),
    ('Pasta','Pasta'),
    ('Cheese','Cheese'),
    ('Pork','Pork'),
    ('Lamb','Lamb'),
    ('Sweet Dessert','Sweet Dessert'),
]

NUMBER_CHOICES = [
    ('','-'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class SearchForm(forms.ModelForm):
    name = forms.CharField(required=False)
    # wine_type = forms.CharField(required=False)
    
    # wine_types = Wine.objects.values('wine_type').filter(wine_type__isnull=False)
    # type_set = set()
    # for t in wine_types:
    #     type_set.add(t['wine_type'])
    # print(type_set)
    # wine_types = Wine.objects.values('food').filter(wine_type__isnull=False)
    # type_set = set()
    # for t in wine_types:
    #     type_set.add(t['food'])
    # print(type_set)
    wine_type = forms.CharField(required=False, widget=forms.Select(choices=TYPE_CHOICES))
    food = forms.CharField(required=False, widget=forms.Select(choices=FOOD_CHOICES))
    sugar = forms.IntegerField(required=False, widget=forms.Select(choices=NUMBER_CHOICES))
    sour = forms.IntegerField(required=False, widget=forms.Select(choices=NUMBER_CHOICES))
    
    class Meta:
        model = Wine
        fields = ['name', 'wine_type', 'food', 'sugar', 'sour']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'wine_type': forms.TextInput(attrs={'class': 'form-control'}),
        #     'sugar': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'sour': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
