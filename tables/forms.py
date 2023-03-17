from django.forms import ModelForm
from .models import Table, Row

#add the header row to the table
class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["title", "desc", "col1", "col2", "col3", "col4", "col5", "status"]

    def __init__(self, *args, **kwargs):
        super(TableForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "input", "placeholder": "Add Title"})
        self.fields['desc'].widget.attrs.update({"class": "input", "placeholder": "Add a cool description (optional)"})
        self.fields['col1'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col2'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col3'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col4'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['col5'].widget.attrs.update({"class": "input", "placeholder": "Add a subject(optional)"})
        self.fields['status'].widget.attrs.update({"class": "input", "placeholder": "Public/Private"})

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
