from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 一覧画面（トップページ）
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 詳細画面
    path('post/new/', views.post_create, name='post_create'),  # 新規投稿
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # 編集画面
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # 削除確認画面
    path('post/<int:pk>/like/', views.post_like, name='post_like'),  # いいね機能（AJAX）
]
