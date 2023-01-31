from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-table/", views.addTable, name="add-table"),
    path("view-tables/", views.viewTables, name="view-tables"),
    path("view-table/<str:pk>/", views.viewTable, name="view-table"),
]