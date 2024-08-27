from .views import ObtainTokenView,PasswordChangeView,PasswordResetView,UserManagementView
from django.urls import path
urlpatterns = [
path('login/', ObtainTokenView.as_view(), name='token_obtain_pair'),
path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
path('password_change/', PasswordChangeView.as_view(), name='password_change'),
path('user_manage/', UserManagementView.as_view(), name='user_manage'),
]

