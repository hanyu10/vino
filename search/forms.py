from django import forms
from wine.models import Wine

def get_choice_list(to_find):
    choice_list = [(None, '-')] # (실제 값, 출력 값)의 리스트
    temp_set = set()
    for e in Wine.objects.values(to_find):
        temp_set.add(list(e.values())[0])
    for e in temp_set:
        choice_list.append((e, e))
    return choice_list

class SearchForm(forms.ModelForm):
    wine_type_choices = get_choice_list('wine_type')
    food_choices = get_choice_list('food')
    sugar_choices = get_choice_list('sugar')
    sour_choices = get_choice_list('sour')

    name = forms.CharField(required=False)
    wine_type = forms.ChoiceField(required=False, 
                    choices=wine_type_choices,)
    food = forms.ChoiceField(required=False, 
                    choices=food_choices,)
    sugar = forms.ChoiceField(required=False, 
                    choices=sugar_choices,)
    sour = forms.ChoiceField(required=False, 
                    choices=sour_choices,)

    class Meta:
        model = Wine
        fields = ['name', 'wine_type', 'food', 'sugar', 'sour']
