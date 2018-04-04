from django import forms
from django.contrib.auth import (
	authenticate, get_user_model, login, logout
)
import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserStudyData
from .util.time import getnow
# Create your models here.

User = get_user_model()

# 국 수 영 과 ... 입력받는 폼
class StatisticsWriteForm(forms.Form):
    math = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '수학 공부 (시간)'}))
    m_math = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '수학 공부 (분)'}))

    korean = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '국어 공부 (시간)'}))
    m_korean = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '국어 공부 (분)'}))

    english = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '영어 공부 (시간)'}))
    m_english = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '영어 공부 (분)'}))

    science = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '과학 공부 (시간)'}))
    m_science = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '과학 공부 (분)'}))

    def clean(self,*args, **kwargs):
        m_math = self.cleaned_data.get('m_math')
        m_korean = self.cleaned_data.get('m_korean')
        m_english = self.cleaned_data.get('m_english')
        m_science = self.cleaned_data.get('m_science')

        if m_math and m_korean and m_english and m_science:
            if (m_math > 59 or m_korean > 59 or m_english > 59 or m_science > 59) or (m_math < 1 or m_korean < 1 or m_english < 1 or m_science < 1):
                raise forms.ValidationError('1 ~ 59 까지만 입력이 가능합니다.')
        return super(StatisticsWriteForm, self).clean(*args, **kwargs)

class CreateUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-Password'}))

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)

        if commit:
            user.save()
        return user

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        # user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not longer active')
        return super(UserLoginForm, self).clean(*args, **kwargs)