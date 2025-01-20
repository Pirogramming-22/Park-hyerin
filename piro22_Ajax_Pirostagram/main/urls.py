from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like-toggle/<int:post_id>/', views.like_toggle, name='like_toggle'),
    path('comment-create/<int:post_id>/', views.comment_create, name='comment_create'),
]
