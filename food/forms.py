from django import forms
from .models import FoodType

class FoodFilterForm(forms.Form):
    type_of_food = forms.ModelChoiceField(queryset=FoodType.objects.all(), empty_label='All', required=False, label='Food type')
    min_price = forms.DecimalField(min_value=0, required=False, label='Min price')
    max_price = forms.DecimalField(min_value=0, required=False, label='Max price')
    search_query = forms.CharField(required=False, label='Search')
