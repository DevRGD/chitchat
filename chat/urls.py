from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # type: ignore
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-mail/', views.password_reset_mail,
         name='password_reset_mail'),
]
