from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect

from apps.users import forms as auth_forms


def login(request):
    form = auth_forms.LoginForm()
    erro = False

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = auth_forms.LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)

            if user:
                auth_login(request, user)
                return redirect(request.GET.get('next', '/'))

        erro = True

    context = {
        'login_form': form,
        'erro': erro
    }
    return render(request, 'core/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('users:login')
