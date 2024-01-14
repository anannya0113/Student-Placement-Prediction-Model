from django.urls import path
from . import views

urlpatterns = [
    path('Predict', views.Predict, name="Predict"),
    path('', views.home, name="home"),
]
