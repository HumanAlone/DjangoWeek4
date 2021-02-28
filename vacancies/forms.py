from django import forms
from django.forms import ModelForm, Textarea, TextInput

from vacancies.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        widgets = {
            'written_cover_letter': Textarea(attrs={'class': 'form-control'}),
            'written_username': TextInput(attrs={'class': 'form-control'}),
            'written_phone': TextInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(forms.Form):
    login = forms.CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
