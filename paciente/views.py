from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from paciente.forms import Novo_Paciente_Form, Atualizar_Paciente_Form
from paciente.models import Paciente

@login_required
def novo_paciente(request):
    form = Novo_Paciente_Form(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_pacientes")

    context = {'form': form}
    return render(request, "novo-paciente.html", context)

@login_required
def listar_paciente(request):
    pacientes = Paciente.objects.all()
    permissao_atualizar = request.user.has_perm('brain.change_paciente')
    permissao_deletar = request.user.has_perm('brain.delete_paciente')

    context = {'pacientes': pacientes, 'permissao_atualizar': permissao_atualizar, 'permissao_deletar': permissao_deletar}
    return render(request, "listar-pacientes.html", context)

@login_required
def atualizar_paciente(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    form = Atualizar_Paciente_Form(request.POST or None, instance=paciente)

    if (form.is_valid()):
        form.save()
        return redirect("listar_pacientes")

    context = {'paciente':paciente, 'form':form}
    return render(request, "novo-paciente.html", context)

@login_required
def deletar_paciente(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)

    if (request.method == 'POST'):
        paciente.delete()
        return redirect("listar_pacientes")

    return render(request, "deletar-paciente.html", {'paciente':paciente})

@login_required
def perfil_paciente(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    

    context = {'paciente':paciente}
    return render(request, "perfil.html", context)