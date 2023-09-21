from django.shortcuts import render, redirect
from .models import Table, Row, Suggestion, Sugrow
from .forms import TableForm, RowForm, SuggestionForm, SugrowForm
from django.contrib.auth.decorators import login_required
from . utils import searchTable, searchRow, orderTable, paginateTable, paginateRow
from users.models import Profile

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    return render(request, "tables/home.html")

@login_required(login_url="login")
def viewTables(request, pk):
    profile=Profile.objects.get(id=pk)
    tables=profile.table_set.all()
    tables, search_query=searchTable(request, tables)
    #custom_range, tables=paginateTable(request, tables, 2)
    d=tables.exclude(desc__isnull=True).count()
    st=tables.exclude(status="Private").count()
    context={"tables":tables, "profile":profile, "search_query":search_query, "d":d, "st":st}
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
    profile=table.owner
    sugs=table.suggestion_set.all()
    rows, search_query=searchRow(request, rows)
    table.getTotal
    rows, order_query=orderTable(request, rows)
    #custom_range, rows=paginateTable(request, rows, 2)
    c=rows.exclude(date__isnull=True).count()
    context={"table":table, "rows":rows, "profile":profile, "search_query":search_query, "order_query":order_query, "c":c, "sugs":sugs}
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
        return redirect("view-tables", profile.id)
    context={"object":table, "rows":table.row_set.all(), "name": "table"}
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
        
    context={"object":row, "name": "row", "rows":row.table_name.row_set.all()}
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

@login_required(login_url="login")
def addSuggestion(request, pk):
    profile=request.user.profile
    table=Table.objects.get(id=pk)
    form=SuggestionForm()

    if request.method=="POST":
        form=SuggestionForm(request.POST)
        if form.is_valid():
            suggestion=form.save(commit=False)
            suggestion.owner=profile
            suggestion.table_name=table
            suggestion.save()

            return redirect("view-suggestion", suggestion.id)
        
    context={"form":form, "name": "add table", "key":"sug"}
    return render(request, "tables/table-form.html", context)

@login_required(login_url="login")
def viewSuggestions(request, pk):
    table=Table.objects.get(id=pk)
    suggestions=table.suggestion_set.all()
    count=suggestions.exclude(desc__isnull=True).count()
    context={"table":table, "sug":suggestions, "count":count}
    return render(request, "tables/view-suggestions.html", context)

@login_required(login_url="login")
def viewSuggestion(request, pk):
    suggestion=Suggestion.objects.get(id=pk)
    table=suggestion.table_name
    rows=suggestion.sugrow_set.all()
    suggestion.getTotal
    suggestion.is_read=True
    c=rows.exclude(date__isnull=True).count()
    context={"sug":suggestion, "table":table, "rows":rows, "c":c}
    return render(request, "tables/view-suggestion.html", context)

@login_required(login_url="login")
def editSug(request, pk):
    sug=Suggestion.objects.get(id=pk)
    form=SuggestionForm(instance=sug)
    
    if request.method == "POST":
        form=SuggestionForm(request.POST, instance=sug)
        if form.is_valid():
            form.save()
            return redirect("view-suggestion", pk)
        
    context={"form":form, "name": "edit table", "key":"usug"}
    return render(request, "tables/table-form.html", context)

@login_required(login_url="login")
def deleteSug(request, pk):
    suggestion=Suggestion.objects.get(id=pk)
    rows=suggestion.sugrow_set.all()
    if request.method == "POST":
        suggestion.delete()
        return redirect("view-table", suggestion.table_name.id)
    
    context={"object":suggestion, "name": "sug", "rows":rows}
    return render(request, "tables/delete.html", context)

def addSugRow(request,pk):
    suggestion=Suggestion.objects.get(id=pk)
    table=suggestion.table_name
    rows=suggestion.sugrow_set.all()
    form=SugrowForm()

    if request.method=="POST":
        form=SugrowForm(request.POST)
        if form.is_valid():
            row=form.save(commit=False)
            row.sug_name=suggestion
            row.save()
            return redirect("view-suggestion", pk)
    
    context={"form":form, "name": "add", "table":suggestion, "title": table.title, "rows":rows}
    return render(request, "tables/row-form.html", context)

def editSugRow(request,tk,pk):
    suggestion=Suggestion.objects.get(id=tk)
    row=Sugrow.objects.get(id=pk)
    rows=suggestion.sugrow_set.all()
    table=suggestion.table_name
    form=SugrowForm(instance=row)

    if request.method=="POST":
        form=SugrowForm(request.POST, instance=row)
        if form.is_valid():
            row=form.save(commit=False)
            row.sug_name=suggestion
            row.save()
            return redirect("view-suggestion", tk)
    
    context={"form":form, "name": "edit", "title": table.title, "rows":rows, "table":suggestion, "key":"usug"}
    return render(request, "tables/row-form.html", context)

@login_required(login_url="login")
def deleteSugRow(request,pk):
    row=Sugrow.objects.get(id=pk)
    suggestion=row.sug_name
    if request.method == "POST":
        row.delete()
        return redirect("view-suggestion", suggestion.id)
        
    context={"object":suggestion, "rows":suggestion.sugrow_set.all(), "table":suggestion}
    return render(request, "tables/delete.html", context)