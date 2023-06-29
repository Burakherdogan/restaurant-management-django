from django.urls import path
from . import views
urlpatterns = [
    path("", views.takeorder),
    path("take-order", views.takeorder),
]
