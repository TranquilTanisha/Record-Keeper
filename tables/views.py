from django.shortcuts import render, redirect
from .models import Table, Row
from .forms import TableForm, RowForm

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

    context={"form":form, "name": "add table"}
    return render(request, "tables/table-form.html", context)

def viewTable(request, pk):
    table=Table.objects.get(id=pk)
    rows=table.row_set.all()
    table.getTotal
    context={"table":table, "rows":rows}
    return render(request, "tables/view-table.html", context)

def editTable(request, pk):
    table=Table.objects.get(id=pk)
    form=TableForm(instance=table)
    if request.method == "POST":
        form=TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect("view-table", pk)
    context={"form":form, "name": "edit table"}
    return render(request, "tables/table-form.html", context)

def deleteTable(request,pk):
    table=Table.objects.get(id=pk)
    if request.method == "POST":
        table.delete()
        return redirect("view-tables")
    context={"object":table, "name": "table"}
    return render(request, "tables/delete.html", context)

def addRow(request,pk):
    table=Table.objects.get(id=pk)
    rows=table.row_set.all()
    form=RowForm()

    if request.method=="POST":
        form=RowForm(request.POST)
        row=form.save(commit=False)
        row.table_name=table
        row.save()
        return redirect("view-table", pk)
    
    context={"form":form, "name": "add", "table":table, "rows":rows}
    return render(request, "tables/row-form.html", context)

def editRow(request, tk, pk):
    row=Row.objects.get(id=pk)
    table=Table.objects.get(id=tk)
    rows=table.row_set.all()
    form=RowForm(instance=row)

    if request.method == "POST":
        form=RowForm(request.POST, instance=row)

        if form.is_valid():
            form.save()
            return redirect("view-table", tk)

    context={"form":form, "table":table, "rows":rows, "name": "edit", "pk":pk}
    return render(request, "tables/row-form.html", context)

def deleteRow(request,pk):
    row=Row.objects.get(id=pk)
    if request.method == "POST":
        row.delete()
        return redirect("view-table", row.table_name.id)
        
    context={"object":row, "name": "row"}
    return render(request, "tables/delete.html", context)