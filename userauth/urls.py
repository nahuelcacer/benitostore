from django.urls import path, include
from .views import RegistroUsuarioView
    
urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
]
