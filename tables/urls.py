from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-table/", views.addTable, name="add-table"),
    path("view-tables/<str:pk>", views.viewTables, name="view-tables"),
    path("view-table/<str:pk>/", views.viewTable, name="view-table"),
    path("edit-table/<str:pk>/", views.editTable, name="edit-table"),
    path("delete-table/<str:pk>/", views.deleteTable, name="delete-table"),

    path("add-row/<str:pk>/", views.addRow, name="add-row"),
    path("edit-row/<str:tk>/<str:pk>/", views.editRow, name="edit-row"),
    path("delete-row/<str:pk>/", views.deleteRow, name="delete-row"),

    path("view-pdf/<str:pk>/", views.view_pdf, name="view-pdf"),
    path("download-pdf/<str:pk>/", views.download_pdf, name="download-pdf"),

    path("view-suggestions/<str:pk>/", views.viewSuggestions, name="view-suggestions"),
    path("view-suggestion/<str:pk>/", views.viewSuggestion, name="view-suggestion"),

    path("add-suggestion/<str:pk>/", views.addSuggestion, name="add-suggestion"),
    path("edit-suggestion/<str:pk>/", views.editSug, name="edit-suggestion"),
    path("delete-suggestion/<str:pk>/", views.deleteSug, name="delete-suggestion"),

    path("add-suggestion-row/<str:pk>/", views.addSugRow, name="add-suggestion-row"),
    path("edit-suggestion-row/<str:tk>/<str:pk>/", views.editSugRow, name="edit-suggestion-row"),
    path("delete-suggestion-row/<str:pk>/", views.deleteSugRow, name="delete-suggestion-row"),
]