from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from contas.forms import CustomUserCreationForm
from contas.models import MyUser
from contas.permissions import grupo_colaborador_required
from core import settings


@login_required
def atualizar_meu_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('home')
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'user_update.html', {'form': form})


@login_required
@grupo_colaborador_required(['administrador', 'colaborador'])
def atualizar_usuario(request, username):
    user = get_object_or_404(MyUser, username=username)
    if request.method == 'POST':
        form = CustomUserCreationForm(
            request.POST, instance=user, user=request.user)
        if form.is_valid():
            usuario = form.save()

            if user.is_active:
                usuario.is_active = True
                print(usuario.is_active)

                send_mail(
                    'Cadastro Aprovado',
                    f'Olá, {usuario.first_name}, seu e-mail foi aprovado na \
                        plataforma.',

                    settings.DEFAULT_FROM_EMAIL,
                    [usuario.email],  # para
                    fail_silently=False,
                )
                messages.success(request, 'O usuário ' + usuario.email + '\
                    foi atualizado com sucesso!')
                return redirect('lista_usuarios')

            usuario.save()
            messages.success(
                request, 'O perfil de usuário foi atualizado com sucesso!')
            return redirect('home')
    else:
        form = CustomUserCreationForm(instance=user, user=request.user)
    return render(request, 'user_update.html', {'form': form})
