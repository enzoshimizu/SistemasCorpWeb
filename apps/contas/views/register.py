from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from contas.forms import CustomUserCreationForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_valid = False
            usuario.save()

            group = Group.objects.get(name='usuario')
            usuario.groups.add(group)

            messages.success(
                request, 'Registrado. Agora faça o login para começar!')
            return redirect('login')
        else:
            # Tratar quando usuario já existe, senhas... etc...
            messages.error(request, 'A senha deve ter pelo menos 1 caractere \
                           maiúsculo, 1 caractere especial e no minimo 8 \
                            caracteres.')
    form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
