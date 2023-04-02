from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from myapp.views import HomeView, NewUserView, TaskListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', NewUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', TaskListView.as_view(), name='tasks'),

]
