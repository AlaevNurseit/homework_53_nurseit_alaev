from django.urls import path
from articles.views import todolist_list, todolist_create, todolist_detail, todolist_update, todolist_delete

urlpatterns = [
    path("todolist/", todolist_list, name="todolist_list"),
    path("todolist/add/", todolist_create, name="todolist_create"),
    path("todolist/detail/<int:pk>/", todolist_detail, name="todolist_detail"),
    path("todolist/update/<int:pk>/", todolist_update, name="todolist_update"),
path("todolist/delete/<int:pk>/", todolist_delete, name="todolist_delete"),
]