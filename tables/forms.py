from django.forms import ModelForm
from .models import Table, Column

#add the header row to the table
class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = "__all__"

    def __init__(self, *args, **kwargs):
            super(TableForm,self).__init__(*args, **kwargs)
            #self.fields['title'].widget.attrs.update({"class": "input", "placeholder": "Add Title"})

            for name, field in self.fields.items():
                field.widget.attrs.update({"class": "input"})
