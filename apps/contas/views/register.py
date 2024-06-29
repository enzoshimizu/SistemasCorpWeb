from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from contas.forms import CustomUserCreationForm
from core import settings


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, user=request.user)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_valid = False
            usuario.is_active = False
            usuario.save()

            group = Group.objects.get(name='usuario')
            usuario.groups.add(group)

            # Envia e-mail para usuário
            send_mail(  # Envia email para usuario
                'Cadastro Plataforma',
                f'Olá, {usuario.first_name}, em breve você receberá um e-mail \
                    de aprovação para usar a plataforma.',
                # De (em produção usar o e-mail que está no settings)
                settings.DEFAULT_FROM_EMAIL,
                [usuario.email],  # para
                fail_silently=False,
            )

            messages.success(request, 'Registrado. Um e-mail foi enviado \
                para administrador aprovar. Aguarde contato')

            return redirect('login')
        else:
            # Tratar quando usuario já existe, senhas... etc...
            messages.error(request, 'A senha deve ter pelo menos 1 caractere \
                           maiúsculo, 1 caractere especial e no minimo 8 \
                            caracteres.')
    form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
