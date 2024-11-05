from django.urls import include, path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
