from django.urls import path
from rest_framework.authtoken import views

from myapp.api.resources import TaskAPIView, TaskCreateAPIView, TaskInfoAPIView, TaskChangeAPIView


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/create/', TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskInfoAPIView.as_view()),
    path('tasks/<int:pk>/change/', TaskChangeAPIView.as_view()),


]