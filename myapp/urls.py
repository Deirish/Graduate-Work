from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from myapp.views import HomeView, NewUserView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', NewUserView.as_view(), name='register'),

]
