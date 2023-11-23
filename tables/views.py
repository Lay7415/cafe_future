from django.shortcuts import render
from .models import Table
from .forms import TableFilterForm

def tables_view(request):
    form = TableFilterForm(request.GET)

    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        table_type = form.cleaned_data.get('table_type')

        queryset = Table.objects.all()

        if min_price:
            queryset = queryset.filter(price__gte=max_price)

        if max_price:
            queryset = queryset.filter(price__lte=min_price)

        if table_type:
            queryset = queryset.filter(type=table_type)

        context = {'tables': queryset, 'form': form}
        return render(request, 'tables/tables.html', context)

    context = {'form': form}
    return render(request, 'tables/tables.html', context)
