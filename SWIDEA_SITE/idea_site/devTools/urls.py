from django.urls import path
from . import views

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),
    path('add/', views.devtool_add, name='devtool_add'),
]
