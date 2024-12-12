# registrations/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('<int:pk>/', views.registration_details, name='registration_details'),
    path('create/', views.registration_create, name='registration_create'),
    path('<int:pk>/edit/', views.registration_update, name='registration_update'),
    path('<int:pk>/delete/', views.registration_delete, name='registration_delete'),
]
