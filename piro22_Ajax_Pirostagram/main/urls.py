from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('toggle_like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('comment-create/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment-delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
