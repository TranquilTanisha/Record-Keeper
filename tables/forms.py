from django.forms import ModelForm
from .models import Table, Row, Suggestion, Sugrow

#add the header row to the table
class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["title", "desc", "status", "col1", "col2", "col3", "col4", "col5"]

    def __init__(self, *args, **kwargs):
        super(TableForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "input", "placeholder": "Add Title"})
        self.fields['desc'].widget.attrs.update({"class": "input", "placeholder": "Add a cool description (optional)"})
        self.fields['col1'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col2'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col3'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col4'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col5'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['status'].widget.attrs.update({"class": "input"})

#add the data of rows to the table
class RowForm(ModelForm):
    class Meta:
        model=Row
        fields=["col1", "col2", "col3", "col4", "col5", "date"]

    def __init__(self, *args, **kwargs):
        super(RowForm,self).__init__(*args, **kwargs)
        #self.fields['title'].widget.attrs.update({"class": "input", "placeholder": "Add Title"})

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

#to add a suggestion
class SuggestionForm(ModelForm):
    class Meta:
        model=Suggestion
        fields=["desc", "col1", "col2", "col3", "col4", "col5"]

    def __init__(self, *args, **kwargs):
        super(SuggestionForm,self).__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs.update({"class": "input", "placeholder": "Add a cool description (optional)"})
        self.fields['col1'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col2'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col3'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col4'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col5'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})

#to add rows in a sugestion
class SugrowForm(ModelForm):
    class Meta:
        model=Sugrow
        fields=["col1", "col2", "col3", "col4", "col5", "date"]

    def __init__(self, *args, **kwargs):
        super(SugrowForm,self).__init__(*args, **kwargs)
        #self.fields['title'].widget.attrs.update({"class": "input", "placeholder": "Add Title"})

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})