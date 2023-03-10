from . models import Table, Row
from django.db.models import Q

def searchTable(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tables = Table.objects.filter(title__icontains=search_query)
    return tables, search_query

def searchRow(request, r):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    rows=r.distinct().filter(
        Q(col1__icontains=search_query) |
        Q(col2__icontains=search_query) |
        Q(col3__icontains=search_query) |
        Q(col4__icontains=search_query) |
        Q(col5__icontains=search_query)
    )
    return rows, search_query

def orderTable(request, t):
    order_query = ""
    if request.GET.get('order_query'):
        order_query = request.GET.get('order_query')
        
    if order_query== "col1":
        rows=t.order_by("col1")
    elif order_query== "col2":
        rows=t.order_by("col2")
    elif order_query== "col3":
        rows=t.order_by("col3")
    elif order_query== "col4":
        rows=t.order_by("col4")
    elif order_query== "col5":
        rows=t.order_by("col5")
    elif order_query== "date":
        rows=t.order_by("date")
    else:
        rows=t.order_by("-created")
    #rows=t.order_by(order_query)
    return rows, order_query