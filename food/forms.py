from django import forms
from .models import FoodType

class FoodFilterForm(forms.Form):
    type_of_food = forms.ModelChoiceField(queryset=FoodType.objects.all(), empty_label='Все', required=False, label='Тип еды')
    min_price = forms.DecimalField(min_value=0, required=False, label='Минимальная цена')
    max_price = forms.DecimalField(min_value=0, required=False, label='Максимальная цена')
    search_query = forms.CharField(required=False, label='Поиск')
