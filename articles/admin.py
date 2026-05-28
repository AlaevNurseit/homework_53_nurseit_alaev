from django.contrib import admin
from .models import ToDolist


class ToDolistAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'execution_date', 'more_detailed_description']
    list_filter = ['status']
    search_fields = ['description']

admin.site.register(ToDolist, ToDolistAdmin)

