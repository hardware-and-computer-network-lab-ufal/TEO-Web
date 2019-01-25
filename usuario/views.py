from django.shortcuts import render, redirect
from django.conf import settings
from usuario.forms import Cadastro_Form, Editar_Perfil_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def cadastro(request):
    form = Cadastro_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {'form': form}
    return render(request, 'cadastro.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect(settings.LOGOUT_URL)

@login_required
def editar_perfil(request):
    form = Editar_Perfil_Form(request.POST or None, instance=request.user)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'editar-perfil.html', context)
