from django.contrib.auth.models import User
from django.db import models

class Column(models.Model):
    class ColumnNames(models.TextChoices):
        new = 'New'
        inProgress = 'In Progress'
        inQA = 'In QA'
        ready = 'Ready'
        done = 'Done'
    owner = models.ForeignKey(User, related_name='Owner_tasks', verbose_name='Owner', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='Executor_tasks', verbose_name='Executor', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    text = models.CharField(max_length=500)
    status = models.CharField(max_length=12, choices=ColumnNames.choices, default=ColumnNames.new)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.text

