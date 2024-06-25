from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from contas.forms import UserChangeForm
from contas.models import MyUser
from contas.permissions import grupo_colaborador_required


@login_required()
def atualizar_meu_usuario(request):
    if request.method == 'POST':
        form = UserChangeForm(
            request.POST, instance=request.user, user=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user, user=request.user)
    return render(request, 'user_update.html', {'form': form})


@login_required()
@grupo_colaborador_required(['administrador', 'colaborador'])
def atualizar_usuario(request, user_id):
    user = get_object_or_404(MyUser, pk=user_id)
    if request.method == 'POST':
        form = UserChangeForm(
            request.POST, instance=user, user=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'O perfil de usuário foi atualizado com sucesso!'
            )
            return redirect('home')
    else:
        form = UserChangeForm(instance=user, user=request.user)
    return render(request, 'user_update.html', {'form': form})
