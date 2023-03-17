from django.db import models
from datetime import datetime, date
from users.models import Profile
import uuid
# Create your models here.

class Table(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title=models.TextField("Title of the table")
    desc=models.TextField("Description",null=True, blank=True)
    col1=models.TextField("Column 1",null=True, blank=True)
    col2=models.TextField("Column 2",null=True, blank=True)
    col3=models.TextField("Column 3",null=True, blank=True)
    col4=models.TextField("Column 4",null=True, blank=True)
    col5=models.TextField("Column 5",null=True, blank=True)
    #date=models.DateField("Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False, null=True, blank=True)
    total=models.IntegerField(default=0, null=True, blank=True)

    TYPE=(('Public', 'Public'), ('Private', 'Private'))
    status=models.CharField(max_length=200, choices=TYPE, default="Public")

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title', '-created']

    @property
    def getTotal(self):
        rows=self.row_set.all()
        total_c=rows.count()
        self.total=total_c
        self.save()

class Row(models.Model):
    table_name=models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    col1=models.TextField("Column 1 entry",null=True, blank=True)
    col2=models.TextField("Column 2 entry",null=True, blank=True)
    col3=models.TextField("Column 3 entry",null=True, blank=True)
    col4=models.TextField("Column 4 entry",null=True, blank=True)
    col5=models.TextField("Column 5 entry",null=True, blank=True)
    date=models.DateField("Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False, null=True, blank=True)
    #total=models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    

    def __str__(self):
        return str(self.date)