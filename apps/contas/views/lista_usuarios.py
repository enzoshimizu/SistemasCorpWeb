from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from contas.models import MyUser
from contas.permissions import grupo_colaborador_required


@login_required
@grupo_colaborador_required(['administrador', 'colaborador'])
def lista_usuarios(request):  # Lista Cliente
    lista_usuarios = MyUser.objects.select_related(
        'perfil').filter(is_superuser=False)
    return render(
        request, 'lista-usuarios.html', {'lista_usuarios': lista_usuarios}
    )
