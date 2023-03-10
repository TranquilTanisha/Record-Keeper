from django.shortcuts import render, redirect
from .models import Table, Row
from .forms import TableForm, RowForm
from django.contrib.auth.decorators import login_required
from . utils import searchTable, searchRow, orderTable

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required(login_url="login")
def viewTables(request):
    profile=request.user.profile
    tables=profile.table_set.all()
    tables, search_query=searchTable(request)
    context={"tables":tables, "search_query":search_query}
    return render(request, "tables/view-tables.html", context)

@login_required(login_url="login")
def addTable(request):
    profile=request.user.profile
    form=TableForm()

    if request.method=="POST":
        form=TableForm(request.POST)
        if form.is_valid():
            table=form.save(commit=False)
            table.owner=profile
            table.save()
            return redirect("view-table", table.id)

    context={"form":form, "name": "add table"}
    return render(request, "tables/table-form.html", context)

def viewTable(request, pk):
    table=Table.objects.get(id=pk)
    rows=table.row_set.all()
    rows, search_query=searchRow(request, rows)
    table.getTotal
    #count=table.date.count()
    rows, order_query=orderTable(request, rows)
    c=rows.exclude(date__isnull=True).count()
    context={"table":table, "rows":rows, "search_query":search_query, "order_query":order_query, "c":c}
    return render(request, "tables/view-table.html", context)

@login_required(login_url="login")
def editTable(request, pk):
    profile=request.user.profile
    table=profile.table_set.get(id=pk)
    form=TableForm(instance=table)
    if request.method == "POST":
        form=TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect("view-table", pk)
    context={"form":form, "name": "edit table"}
    return render(request, "tables/table-form.html", context)

@login_required(login_url="login")
def deleteTable(request,pk):
    profile=request.user.profile
    table=profile.table_set.get(id=pk)
    if request.method == "POST":
        table.delete()
        return redirect("view-tables")
    context={"object":table, "name": "table"}
    return render(request, "tables/delete.html", context)

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def deleteRow(request,pk):
    row=Row.objects.get(id=pk)
    if request.method == "POST":
        row.delete()
        return redirect("view-table", row.table_name.id)
        
    context={"object":row, "name": "row"}
    return render(request, "tables/delete.html", context)

def view_pdf(request,pk):
    table=Table.objects.get(id=pk)
    rows=table.row_set.all()
    table.getTotal
    c=rows.exclude(date__isnull=True).count()
    context={"table":table, "rows":rows, "c":c}

    template_path="tables/view-pdf.html"
    response=HttpResponse(content_type="application/pdf")
    response["Content-Disposition"]="filename='%s.pdf'" %table.title
    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>"+html+"</pre>")
    return response

def download_pdf(request,pk):
    table=Table.objects.get(id=pk)
    rows=table.row_set.all()
    table.getTotal
    context={"table":table, "rows":rows}
    filename=table.title

    template_path="tables/view-pdf.html"
    response=HttpResponse(content_type='application/pdf')
    response["Content-Disposition"]="attachment; filename=%s.pdf " % filename
    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>"+html+"</pre>")
    return response
