from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('win', views.win),
    path('ad', views.admin),
]
