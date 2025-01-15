from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='list'),
    path('create/', views.idea_create, name='create'),
    path('<int:pk>/', views.idea_detail, name='detail'),
    path('<int:pk>/update/', views.idea_update, name='update'),
    path('<int:pk>/delete/', views.idea_delete, name='delete'),
    path('<int:pk>/interest/', views.idea_interest, name='idea_interest'),
    path('toggle-star/<int:idea_id>/', views.toggle_star, name='toggle_star'),
]