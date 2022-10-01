from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('count', views.count),
    path('win', views.win)
]
