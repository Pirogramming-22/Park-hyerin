from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('add/', views.idea_add, name='idea_add'),
]
