from django.urls import path, include
from .views import RegistroUsuarioView
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView
    
urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('', include('dj_rest_auth.urls')),
    path('password/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password/change/', PasswordChangeView.as_view(), name='password_change')
]
