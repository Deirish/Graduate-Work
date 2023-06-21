from django.urls import path, include
from rest_framework.authtoken import views
from myapp.api.resources import *


urlpatterns = [
    path('tasks', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', TaskInfoAPIView.as_view()),
    path('tasks/create', TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/change/', TaskChangeAPIView.as_view()),
    path('tasks/<int:pk>/task_up/', TaskStatusChangeAPIView.as_view()),
    path('tasks/<int:pk>/task_down/', TaskStatusChangeAPIView.as_view()),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view()),
]