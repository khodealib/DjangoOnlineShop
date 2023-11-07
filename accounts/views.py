import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from DjangoOnlineShop import settings
from accounts.forms import UserRegistrationForm, VerifyCodeForm
from accounts.models import OtpCode, User
from utils.otp import send_otp_code, send_otp_code_fake


class UserRegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_number = random.randint(1000, 9999)
            if settings.DEBUG:
                send_otp_code_fake(form.cleaned_data['phone'], random_number)
            else:
                send_otp_code(form.cleaned_data['phone'], random_number)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_number)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verify_code')
        return render(request, 'accounts/register.html', {'form': form})


class UserRegistrationVerifyCode(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            if code_instance.code == form.cleaned_data['code']:
                if not code_instance.is_expire:
                    User.objects.create_user(
                        phone_number=user_session['phone_number'],
                        email=user_session['email'],
                        full_name=user_session['full_name'],
                        password=user_session['password']
                    )
                    code_instance.delete()
                    messages.success(request, 'User registration successfully', 'success')
                    return redirect('home:index')
                else:
                    code_instance.delete()
                    messages.error(
                        request,
                        'this code is expire, please complete register form again.',
                        'danger'
                    )
                    return redirect('accounts:user_register')
            messages.error(request, 'this code is wrong', 'danger')
            return redirect('accounts:verify_code')
        return redirect('home:index')
