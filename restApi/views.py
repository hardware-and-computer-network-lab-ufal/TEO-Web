from django.shortcuts import render
import paciente.models
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from restApi.serializers import PacienteSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
	queryset = paciente.models.Paciente.objects.all()
	serializer_class = PacienteSerializer

	# def post(self, request):
	# 	print(queryset.data)
	# 	return Response({"id": 'PacienteViewSet', "data": '1234'})

@api_view(['GET','POST'])
def jogo_detail(request):
	if request.method == 'GET':
		pessoa = paciente.models.Paciente.objects.raw('SELECT cpf,nome FROM paciente_paciente WHERE nome = "Menino"')
		serializer = PacienteSerializer(pessoa, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = PacienteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
