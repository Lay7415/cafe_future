from django.urls import path
from . import views

urlpatterns = [
    path('tables/', view=views.tables_view, name='tables'),
    path('reserved/<int:table_id>/', view=views.reserved_tables, name='reserved_tables'),

]
