from django.contrib import admin
from .models import Table, Row, Suggestion, Sugrow
# Register your models here.

admin.site.register(Table)
admin.site.register(Row)
admin.site.register(Suggestion)
admin.site.register(Sugrow)
