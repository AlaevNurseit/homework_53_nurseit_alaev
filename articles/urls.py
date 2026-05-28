from django.urls import path
from articles.views import todolist_list, todolist_create, todolist_detail

urlpatterns = [
    path("todolist/", todolist_list, name="todolist_list"),
    path("todolist/add/", todolist_create, name="todolist_create"),
    path("todolist/detail/<int:pk>/", todolist_detail, name="todolist_detail"),
]