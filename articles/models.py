from django.db import models

class ToDolist(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]
    description = models.TextField(null=False, blank=False, verbose_name="описание")
    status = models.CharField(max_length=300, null=False, blank=False, verbose_name="статус")
    execution_date = models.DateField(null=True, blank=True, verbose_name="дата выполнения")
    more_detailed_description = models.TextField(null=True, blank=True, verbose_name="более подробное описание")


    def __str__(self):
        return self.description[:50]

    class Meta:
        db_table = "todolist"
        verbose_name = "задача"

