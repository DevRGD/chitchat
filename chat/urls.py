from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    # type: ignore
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
         redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),  # type: ignore
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-mail/', views.password_reset_mail,
         name='password_reset_mail'),
]
