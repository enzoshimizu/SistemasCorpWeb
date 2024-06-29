from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from base.utils import add_form_errors_to_messages
from contas.forms import CustomUserCreationForm
from contas.permissions import grupo_colaborador_required
from perfil.forms import PerfilForm


@login_required
@grupo_colaborador_required(['administrador', 'colaborador'])
def adicionar_usuario(request):
    user_form = CustomUserCreationForm(user=request.user)
    perfil_form = PerfilForm(user=request.user)

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, user=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES)

        if user_form.is_valid() and perfil_form.is_valid():
            # Salve o usuário
            usuario = user_form.save()

            group = Group.objects.get(name='usuario')
            usuario.groups.add(group)

            # Crie um novo perfil para o usuário
            perfil = perfil_form.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            messages.success(request, 'Usuário adicionado com sucesso.')
            return redirect('lista_usuarios')
        else:
            add_form_errors_to_messages(request, user_form)
            add_form_errors_to_messages(request, perfil_form)

    context = {'user_form': user_form, 'perfil_form': perfil_form}
    return render(request, "adicionar-usuario.html", context)
