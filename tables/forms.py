from django import forms
from .models import ReservedTable
from .models import Table


class TableFilterForm(forms.Form):
    table_type = forms.ChoiceField(
        choices=[('', 'All')] + Table.type_choices,
        label='Table type',
        required=False,
    )

    min_price = forms.IntegerField(
        label='Min price',
        required=False,
        min_value=0,
    )
    max_price = forms.IntegerField(
        label='Max price',
        required=False,
        min_value=0,
        initial=5000,
    )


class ReservedTableForm(forms.ModelForm):
    class Meta:
        model = ReservedTable
        fields = ['user', 'table', 'data', 'duration']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
