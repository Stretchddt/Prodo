from django.urls import path, include
from .views import TodoList, TodoDetail

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('edit/<str:pk>/', TodoDetail.as_view(), name='todo-detail'),
]