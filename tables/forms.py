from django import forms
from .models import Table


class TableFilterForm(forms.Form):
    min_price = forms.IntegerField(
        label='Минимальная цена',
        required=False,
        min_value=0,
    )
    max_price = forms.IntegerField(
        label='Максимальная цена',
        required=False,
        min_value=0,
        initial=5000,
    )
    table_type = forms.ChoiceField(
        choices=[('', 'Все')] + Table.type_choices,
        label='Тип стола',
        required=False,
    )
