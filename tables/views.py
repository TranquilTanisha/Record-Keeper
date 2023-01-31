from django.shortcuts import render, redirect
from .models import Table, Column
from .forms import TableForm

# Create your views here.
def home(request):
    return render(request, "tables/home.html")

def viewTables(request):
    tables=Table.objects.all()
    context={"tables":tables}
    return render(request, "tables/view-tables.html", context)

def addTable(request):
    form=TableForm()

    if request.method=="POST":
        form=TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context={"form":form}
    return render(request, "tables/add-table.html", context)

def viewTable(request, pk):
    table=Table.objects.get(id=pk)
    columns=table.column.all()
    context={"table":table, "columns":columns}
    return render(request, "tables/view-table.html", context)

