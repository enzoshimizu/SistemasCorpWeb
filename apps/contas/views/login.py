from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.requires_password_change():
                msg = 'Olá '+user.first_name+', como você pode perceber \
                    atualmente a sua senha é 123 cadastrado. Recomendamos \
                    fortemente que você altere sua senha para garantir a \
                    segurança da sua conta. É importante escolher uma senha \
                    forte e única que não seja fácil de adivinhar. Obrigado \
                    pela sua atenção!'
                messages.warning(request, msg)
                # Vai para rota de alterar senha.
                return redirect('force_password_change')
            else:
                return redirect('home')
        else:
            messages.error(
                request,
                'Combinação de e-mail e senha inválida. Se o erro persistir, \
                entre em contato com o administrador do sistema.'
            )
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')
