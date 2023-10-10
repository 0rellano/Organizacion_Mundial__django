from django.urls import path
from organizacion_mundial import views

urlpatterns = [
    path('', views.index),
    path('paises/', views.ListaPaises.as_view()),
    path('pais/<int:pk>', views.PaisView.as_view())
]