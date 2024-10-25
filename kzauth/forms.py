
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
  username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class' : 'form-input'}))
  password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class' : 'form-input'}))

  class Meta:
    model = get_user_model()
    #fields = ['username','password']

class RegForm(UserCreationForm):
  username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class' : 'form-input'}))
  password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class' : 'form-input'}))
  password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class' : 'form-input'}))

  class Meta:
    model = get_user_model()
    fields = ['username','email','password1','password2']
    labels={
      'email':'E-mail'
    }
    widgets = {
      'email' : forms.TextInput(attrs={'class' : 'form-input'})
    }
  
  def clean_email(self):
    email = self.cleaned_data['email']
    if get_user_model().objects.filter(email=email).exist():
      raise forms.ValidationError('Пользователь с таким адресом email уже зарегестрирован')
    return email