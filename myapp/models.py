from django.contrib.auth.models import User
from django.db import models


TASK = (
    (1, 'New'),
    (2, 'In Progress'),
    (3, 'In QA'),
    (4, 'Ready'),
    (5, 'Done')
)

class Column(models.Model):

    owner = models.ForeignKey(User, related_name='Owner_tasks', verbose_name='Owner', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='Executor_tasks', verbose_name='Executor', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    text = models.CharField(max_length=500)
    status = models.IntegerField(choices=TASK, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.text

