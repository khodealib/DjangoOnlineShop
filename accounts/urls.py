from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('register/verify/', views.UserRegistrationVerifyCode.as_view(), name='user_register_verify'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('login/verify', views.UserLoginVerifyCode.as_view(), name='user_login_verify'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
