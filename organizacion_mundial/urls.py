from django.urls import path
from organizacion_mundial import views

urlpatterns = [
    path('', views.index)
]