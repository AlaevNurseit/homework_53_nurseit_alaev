from django import forms
from django.forms import TextInput
from articles.models import ToDolist

class TodolistForm(forms.ModelForm):
    description = forms.CharField(widget=TextInput(attrs={"class": "form-control","cols": "40", "rows": "50"}),required=True, label="Описание", error_messages={"required": "обязательно поле для заполнения"})
    more_detailed_description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "cols": "40", "rows": "10"}), required=False, label="Подробное описание")
    status = forms.ChoiceField(choices=ToDolist.STATUS_CHOICES, widget=forms.Select(attrs={"class": "form-select"}), required=True, label="Статус")
    execution_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}), required=False, label="Дата выполнения")

    class Meta:
        model = ToDolist
        fields = ('description', 'more_detailed_description', 'status', 'execution_date')