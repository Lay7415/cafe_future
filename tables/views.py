from django.shortcuts import render
from .models import Table, ReservedTable
from .forms import TableFilterForm

def tables_view(request):
    form = TableFilterForm(request.GET)
    tables = Table.objects.all()

    if form.is_valid():
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        table_type = form.cleaned_data['table_type']

        if table_type:
            tables = tables.filter(type=table_type)
            
        if min_price:
            tables = tables.filter(price__gte=min_price)

        if max_price:
            tables = tables.filter(price__lte=max_price)


    return render(request, 'tables/tables.html', {'form': form, 'tables': tables})


def reserved_tables(request, table_id):
    table = Table.objects.filter(id=table_id)
    reserved_tables = ReservedTable.objects.filter(table__id=table_id)
    context = {'reserved_tables': reserved_tables, "table": table}
    
    
    return render(request, 'tables/reserved_tables.html', context)

