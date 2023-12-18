from django import forms


class FoodFilterForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search')
