from django.contrib import admin
from .models import Table, ReservedTable

admin.site.register(Table)
admin.site.register(ReservedTable)

# Register your models here.