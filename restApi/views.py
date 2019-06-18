from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from restApi.serializers import PacienteSerializer,PacienteJogaSerializer
from restApi.serializers import JogosSerializer
import paciente.models
# import jogos.models

# Retorna todos os pacientes
class PacienteViewSet(viewsets.ModelViewSet):
	queryset = paciente.models.Paciente.objects.all()
	serializer_class = PacienteSerializer

@api_view(['GET', 'POST'])
def paciente_joga(request):
	if request.method == 'GET':
		if request.method == 'GET':
			if request.GET.get('cpf', '') == '':
				return Response(status=status.HTTP_400_BAD_REQUEST)
		pessoaJoga = paciente.models.PacienteJoga.objects.raw('SELECT id,tempoDejogo,cpf_id,nome_id FROM paciente_pacientejoga WHERE cpf_id = ' + request.GET.get('cpf', ''))
		serializer = PacienteJogaSerializer(pessoaJoga, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = PacienteJogaSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		if serializer.errors['non_field_errors'][0] == "Os campos nome, cpf devem criar um set único.":
			rowJogo = paciente.models.PacienteJoga.objects.get(cpf_id=serializer.data['cpf'], nome_id=serializer.data['nome'])
			rowJogo.tempoDeJogo += int(serializer.data['tempoDeJogo'])
			data = {
				"id": rowJogo.id,
				"tempoDeJogo": rowJogo.tempoDeJogo,
				"cpf": str(rowJogo.cpf.cpf),
				"nome": str(rowJogo.nome),
			}
			new_input = PacienteJogaSerializer(rowJogo, data=data)
			if new_input.is_valid():
				new_input.save()
				return Response(new_input.data, status=status.HTTP_201_CREATED)
			return Response(new_input.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'PUT':
		print("ola")
	elif request.method == 'DELETE':
		print("ola")


# @api_view(['GET','POST'])
# def jogo_detail(request):
# 	if request.method == 'GET':
# 		if request.GET.get('cpf', '') == '':
# 			return Response(status=status.HTTP_400_BAD_REQUEST)
# 		pessoaJoga = paciente.models.PacienteJoga.objects.raw('SELECT id,tempoDejogo,cpf_id,nome_id FROM paciente_pacientejoga WHERE cpf_id = ' + request.GET.get('cpf', ''))
# 		# pessoa = paciente.models.Paciente.objects.raw('SELECT id,tempoDejogo,cpf_id,nome_id FROM paciente_pacientejoga WHERE id = 1')
# 		# + request.GET.get('cpf', '')
# 		# jogos = jogos.models.Jogos.objects.all()
		
# 		serializer = PacienteJogaSerializer(pessoaJoga, many=True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		serializer = PacienteSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
