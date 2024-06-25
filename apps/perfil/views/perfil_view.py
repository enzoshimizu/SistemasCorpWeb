from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render


def perfil_view(request, username):
    User = get_user_model()
    perfil = get_object_or_404(User, username=username)
    context = {'obj': perfil}
    return render(request, 'perfil.html', context)
