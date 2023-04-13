from django.urls import path
from rest_framework.authtoken import views

from myapp.api.resources import ColumnAPIView


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('tasks/', ColumnAPIView.as_view()),

]