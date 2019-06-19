from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from restApi.serializers import PacienteSerializer,PacienteJogaSerializer
from restApi.serializers import JogosSerializer
from paciente.models import PacienteJoga, Paciente
import json

# Retorna todos os pacientes
class PacienteViewSet(viewsets.ModelViewSet):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer

@api_view(['GET', 'POST'])
def paciente_joga(request):
	if request.method == 'GET':
		if request.method == 'GET':
			if request.GET.get('cpf', '') == '':
				return Response(status=status.HTTP_400_BAD_REQUEST)
		pessoaJoga = PacienteJoga.objects.raw('SELECT id,cpf_id,nomeJogo_id,tempojogo,quantidadeAcertos,quantidadeErros FROM paciente_pacientejoga WHERE cpf_id = ' + request.GET.get('cpf', ''))
		serializer = PacienteJogaSerializer(pessoaJoga, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = PacienteJogaSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def jogos_estatisticas(request):
	query = PacienteJoga.objects.all()
	
	userJogo = {}
	for x in query:
		userJogo[str(x.cpf.cpf)+str(x.nomeJogo)] = [None, None, 0, 0, 0]

	for x in query:
		qtdTempo = int(userJogo[str(x.cpf.cpf)+str(x.nomeJogo)][2])
		qtdAcertos = int(userJogo[str(x.cpf.cpf)+str(x.nomeJogo)][3])
		qtdErros = int(userJogo[str(x.cpf.cpf)+str(x.nomeJogo)][4])
		userJogo[str(x.cpf.cpf)+str(x.nomeJogo)] = [str(x.cpf.cpf), str(x.nomeJogo), (qtdTempo+int(x.tempoJogo)), (qtdAcertos+int(x.quantidadeAcertos)), (qtdErros+int(x.quantidadeErros))]
	
	# data = {
	# 	'cpf': userJogo[0],
	# 	'nomeJogo': userJogo[1],
	# 	'tempoTotalJogo': userJogo[2],
	# 	'quantidadeTotalAcertos': userJogo[3],
	# 	'quantidadeTotalErros': userJogo[4],
	# }

	data = []
	for x in userJogo:
		row = {}
		
		row['cpf'] = userJogo[x][0]
		row['nomeJogo'] = userJogo[x][1]
		row['tempoTotalJogo'] = userJogo[x][2]
		row['quantidadeTotalAcertos'] = userJogo[x][3]
		row['quantidadeTotalErros'] = userJogo[x][4]
		data.append(row)
		
	return Response(data)







# @api_view(['GET','POST'])
# def jogo_detail(request):
# 	if request.method == 'GET':
# 		if request.GET.get('cpf', '') == '':
# 			return Response(status=status.HTTP_400_BAD_REQUEST)
# 		pessoaJoga = jogos.models.JogosEstatisticas.objects.raw('SELECT id,tempoDejogo,cpf_id,nome_id FROM paciente_JogosEstatisticas WHERE cpf_id = ' + request.GET.get('cpf', ''))
# 		# pessoa = jogos.models.Paciente.objects.raw('SELECT id,tempoDejogo,cpf_id,nome_id FROM paciente_JogosEstatisticas WHERE id = 1')
# 		# + request.GET.get('cpf', '')
# 		# jogos = jogos.models.Jogos.objects.all()
		
# 		serializer = JogosEstatisticasSerializer(pessoaJoga, many=True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		serializer = PacienteSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
