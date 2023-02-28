from . models import Table, Row
from django.db.models import Q

def searchTable(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tables = Table.objects.filter(title__icontains=search_query)
    return tables, search_query

def searchRow(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    rows=Row.objects.distinct().filter(
        Q(col1__icontains=search_query) |
        Q(col2__icontains=search_query) |
        Q(col3__icontains=search_query) |
        Q(col4__icontains=search_query) |
        Q(col5__icontains=search_query)
    )
    return rows, search_query