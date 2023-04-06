from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from myapp.views import HomeView, NewUserView, TaskListView, TaskCreateView, TaskSearchView, TaskChangeView, \
    TaskDownView, TaskUpView, TaskDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', NewUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('task_create/', TaskCreateView.as_view() , name='task_create'),
    path('task_search/', TaskSearchView.as_view(), name='task_search'),
    path('tasks/task_change/<int:pk>/', TaskChangeView.as_view(), name='change'),
    path('tasks/task_up/<int:pk>/', TaskUpView.as_view(), name='up'),
    path('tasks/task_down/<int:pk>/', TaskDownView.as_view() , name='down'),
    path('tasks/task_delete/<int:pk>/', TaskDeleteView.as_view(), name='delete')

]
