from django.urls import path
from account.views import (
    user_registration_view,
    user_login_view,
    user_profile_view,
    user_change_password_view,
    send_password_reset_email_view,
    user_password_reset_view,
)

urlpatterns = [
    path('register/', user_registration_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('profile/', user_profile_view, name='profile'),
    path('changepassword/', user_change_password_view, name='changepassword'),
    path('send-reset-password-email/', send_password_reset_email_view, name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', user_password_reset_view, name='reset-password'),
]
