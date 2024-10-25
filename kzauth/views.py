from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from kzauth.forms import LoginForm, RegForm

class LoginUser(LoginView):
  form_class = LoginForm
  template_name = 'kzauth/login.html'
  extra_content = {'title':'Авторизация'}

  #def get_success_url(self):
  #  return reverse_lazy('index')

class RegUser(CreateView):
  form_class = RegForm
  template_name = 'kzauth/reg.html'
  extra_context = {'title':'Регистрация'}
  success_url = reverse_lazy('kzauth:login')



#def regUser(request):
#  if request.method == 'POST':
#    form = RegForm(request.POST)
#    if form.is_valid():
#      user = form.save(commit=False)
#      user.set_password(form.cleaned_data['password'])
#      user.save()
#      return render(request, 'index')
#  else:
#    form = RegForm()
#  return render(request, 'kzauth/reg.html', {'form':form})