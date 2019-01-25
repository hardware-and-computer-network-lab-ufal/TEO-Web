from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from clinica.forms import Nova_Clinica_Form, Atualizar_Clinica_Form
from clinica.models import Clinica

@login_required
def nova_clinica(request):
    form = Nova_Clinica_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_clinicas")

    context = {'form': form}
    return render(request, "nova-clinica.html", context)

@login_required
def listar_clinica(request):
    clinicas = Clinica.objects.all()
    permissao_atualizar = request.user.has_perm('clinica.change_clinica')
    permissao_deletar = request.user.has_perm('clinica.delete_clinica')
    context = {'clinicas': clinicas, 'permissao_atualizar': permissao_atualizar, 'permissao_deletar': permissao_deletar}
    return render(request, "listar-clinicas.html", context)

@login_required
def atualizar_clinica(request, cnpj):
    clinica = Clinica.objects.get(cnpj=cnpj)
    form = Atualizar_Clinica_Form(request.POST or None, instance=clinica)

    if (form.is_valid()):
        form.save()
        return redirect("listar_clinicas")

    context = {'form': form, 'clinica': clinica}
    return render(request, "nova-clinica.html", context)

@login_required
def deletar_clinica(request, cnpj):
    clinica = Clinica.objects.get(cnpj=cnpj)

    if (request.method == 'POST'):
        clinica.delete()
        return redirect('listar_clinicas')

    return render(request, "deletar-clinica.html", {'clinica':clinica})
