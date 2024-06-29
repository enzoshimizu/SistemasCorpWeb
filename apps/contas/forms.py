import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from contas.models import MyUser
import random
import string


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(
        label="Confirmação de Senha",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'email': 'Email',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'is_active': 'Usuário Ativo?'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            del self.fields['password1']
            del self.fields['password2']

        for field_name, field in self.fields.items():
            if field.widget.__class__ in [
                forms.CheckboxInput, forms.RadioSelect
            ]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

        def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            if len(password1) < 8:
                raise forms.ValidationError(
                    "A senha deve conter pelo menos 8 caracteres.")

            # Verifique se a senha contém pelo menos uma letra maiúscula,
            # uma letra minúscula e um caractere especial
            maiusculas = re.search(r'[A-Z]', password1)
            minusculas = re.search(r'[a-z]', password1)
            caract_esp = re.search(r'[!@#$%^&*(),.?":{}|<>]', password1)
            if not maiusculas or not minusculas or not caract_esp:
                raise forms.ValidationError(
                    "A senha deve conter pelo menos 8 caracteres, uma \
                    letra maiúscula, uma letra minúscula e um caractere \
                    especial.")
            return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Senhas não estão iguais!")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.user and self.user.is_authenticated:
            password = ''.join(random.choices(string.digits, k=6))
            user.set_password(password)
            user.force_change_password = True

            send_mail(
                'Sua senha provisória',
                f'Sua senha provisória para entrar na plataforma é: {
                    password}',
                'email@email.com',  # Substitua pelo seu e-mail configurado
                [user.email],
                fail_silently=False,
            )
        else:
            user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
