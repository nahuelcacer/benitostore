from django.urls import path, include
from .views import RegistroUsuarioView
from dj_rest_auth.views import LoginView
    
urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login')
]
