from django.shortcuts import render
from .models import Table, ReservedTable
from .forms import TableFilterForm, ReservedTableForm
from access_management.models import User


def tables_view(request):
    auth = request.user.id
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

    return render(request, 'tables/tables.html', {'form': form, 'tables': tables, 'auth': auth})


def reserved_tables(request, table_id):
    auth = request.user.id
    user = User.objects.get(id=auth)
    table = Table.objects.get(id=table_id)
    reserved_tables = ReservedTable.objects.all()
    form = ReservedTableForm()
    context = {'reserved_tables': reserved_tables,
               "table": table, 'auth': auth, "user": user, "form": form}

    return render(request, 'tables/reserved_tables.html', context)
