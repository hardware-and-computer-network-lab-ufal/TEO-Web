from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profissional.models import Profissional
from profissional.forms import Novo_Profissional_Form, Atualizar_Profissional_Form
from clinica.models import Clinica

@login_required
def novo_profissional(request):
    form = Novo_Profissional_Form(request.POST or None)
    clinicas = Clinica.objects.all()

    if form.is_valid():
        form.save()
        return redirect("listar_profissionais")

    context = {'form': form, 'clinicas': clinicas}
    return render(request, "novo-profissional.html", context)

@login_required
def listar_profissional(request):
    profissionais = Profissional.objects.all()
    permissao_atualizar = request.user.has_perm('brain.change_profissional')
    permissao_deletar = request.user.has_perm('brain.delete_profissional')
    context = {'profissionais': profissionais, 'permissao_atualizar': permissao_atualizar, 'permissao_deletar': permissao_deletar}
    return render(request, "listar-profissionais.html", context)

@login_required
def atualizar_profissional(request, cpf):
    profissional = Profissional.objects.get(cpf=cpf)
    form = Atualizar_Profissional_Form(request.POST or None, instance=profissional)
    clinicas = Clinica.objects.all()

    if (form.is_valid()):
        form.save()
        return redirect("listar_profissionais")

    context = {'profissional':profissional, 'form':form, 'clinicas': clinicas}
    return render(request, "novo-profissional.html", context)

@login_required
def deletar_profissional(request, cpf):
    profissional = Profissional.objects.get(cpf=cpf)

    if (request.method == 'POST'):
        profissional.delete()
        return redirect("listar_profissionais")

    return render(request, "deletar-profissional.html", {'profissional':profissional})
