from django import forms
from django.core.exceptions import ValidationError

from apps.users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'name@example.com',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primeiro nome',
        required=True,
        # error_messages='Insira um nome válido',
        empty_value='O nome é obrigatório',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'João',
            }
        )
    )
    last_name = forms.CharField(
        label='Sobrenome',
        required=True,
        # error_messages='Insira um sobrenome válido',
        empty_value='O sobrenome é obrigatório',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Silva',
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        # error_messages='Insira um email válido',
        empty_value='O e-mail é obrigatório',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'name@example.com',
            }
        )
    )
    password1 = forms.CharField(
        label='Senha',
        required=True,
        error_messages={
            'password': 'As senhas precisam ser iguais'
        },
        empty_value='Insira uma senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmação de senha',
        required=True,
        error_messages={
            'password': 'As senhas precisam ser iguais'
        },
        empty_value='Insira uma senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError('As senhas precisam ser iguais')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError('As senhas precisam ser iguais')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        if self.errors:
            for field in self.fields:
                if field in self.errors:
                    self.fields[field].widget.attrs['class'] += ' invalid'
