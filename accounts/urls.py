from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('verify/', views.UserRegistrationVerifyCode.as_view(), name='verify_code'),
]
