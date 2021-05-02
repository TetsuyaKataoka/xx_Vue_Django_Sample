from django.urls import include, path
from .views import *

app_name = 'api'

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
]