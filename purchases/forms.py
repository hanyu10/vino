from django import forms
from .models import Shop

def get_choice_list(to_find):
    choice_list = [(None, '-')] # (실제 값, 출력 값)의 리스트
    temp_set = set()
    for e in Shop.objects.values(to_find):
        temp_set.add(list(e.values())[0])
    for e in temp_set:
        choice_list.append((e, e))
    return choice_list

class ShopForm(forms.ModelForm):
    shop_name_choices = get_choice_list('name')
    shop_area_choices = get_choice_list('area')

    name = forms.CharField(required=False)
    area = forms.ChoiceField(required=False, 
                    choices=shop_area_choices,)

    class Meta:
        model = Shop
        fields = ['name', 'area']
