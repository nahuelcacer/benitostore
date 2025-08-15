from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  UserSerializer
# Create your views here.
#crea el rest api view para registarse y que ademas de registrar el user agrege los datos de envio
class RegistroUsuarioView(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            # Aquí puedes agregar la lógica para guardar los datos de envío
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
