from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput, EmailField, EmailInput


class SignInForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'name': 'username',
                'id': 'username',
                'type': 'text',
                'required': 'required'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'password',
                'id': 'password',
                'type': 'password',
                'required': 'required'
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'name': 'username',
                'id': 'username',
                'type': 'text',
                'required': 'required'
            }
        )
    )
    password1 = CharField(
        strip=False,
        widget=PasswordInput(
            attrs={
                'name': 'password',
                'id': 'password',
                'type': 'password',
                'required': 'required'
            }
        )
    )
    password2 = CharField(
        strip=False,
        widget=PasswordInput(
            attrs={
                'name': 'cpassword',
                'id': 'cpassword',
                'type': 'password',
                'required': 'required'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'name': 'email',
                'id': 'email',
                'type': 'email',
                'required': 'required'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email')
