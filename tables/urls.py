from django.urls import path
from . import views

urlpatterns = [
    path("add-table/", views.addTable, name="add-table"),
    path("", views.viewTables, name="view-tables"),
    path("view-table/<str:pk>/", views.viewTable, name="view-table"),
    path("edit-table/<str:pk>/", views.editTable, name="edit-table"),
    path("delete-table/<str:pk>/", views.deleteTable, name="delete-table"),

    path("add-row/<str:pk>/", views.addRow, name="add-row"),
    path("edit-row/<str:tk>/<str:pk>/", views.editRow, name="edit-row"),
    path("delete-row/<str:pk>/", views.deleteRow, name="delete-row"),

    path("view-pdf/<str:pk>/", views.view_pdf, name="view-pdf"),
    path("download-pdf/<str:pk>/", views.download_pdf, name="download-pdf"),
]