from django.urls import path, include
from rest_framework import routers
from myapp.api.resources import *


router = routers.SimpleRouter()
router.register()


urlpatterns = [
    path("api/", include('myapp.api.urls'))
]