# _*_ coding: utf-8 _*_
__date__ = '2018/4/22 下午8:52'
from django import forms
from captcha.fields import CaptchaField

from models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']


