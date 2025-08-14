from django.urls import path, include
from .views import RegistroUsuarioView
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView
    
urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('', include('dj_rest_auth.urls')),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password/change/', PasswordChangeView.as_view(), name='password_change')
]
