from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path("profiles/", views.profiles, name='profiles'),
    path("user-profile/<str:pk>/", views.userprofile, name='user-profile'),
    path("account/", views.userAccount, name='account'),
    path("edit-account/", views.editAccount, name='edit-account'),
]