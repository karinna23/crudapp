from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]