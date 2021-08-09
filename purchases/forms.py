from django import forms
from wine.models import Shop


def get_choice_list(to_find):
    choice_list = [(None, '-')] # (실제 값, 출력 값)의 리스트
    temp_set = set()
    for e in Shop.objects.values(to_find):
        temp_set.add(list(e.values())[0])
    for e in temp_set:
        choice_list.append((e, e))
    return choice_list

class SearchForm(forms.ModelForm):
    shop_name_choices = get_choice_list('shop_name')
    shop_area_choices = get_choice_list('shop_area')
    shop_address_choices = get_choice_list('shop_area')


    shop_name = forms.CharField(required=False)
    shop_area = forms.ChoiceField(required=False, 
                    choices=shop_area_choices,)
    shop_address = forms.ChoiceField(required=False, 
                    choices=shop_address_choices,)
                    
   

    class Meta:
        model = Shop
        fields = ['shop_name', 'shop_area']
