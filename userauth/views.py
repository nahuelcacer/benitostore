from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DatosEnvioSerializer, UserSerializer
# Create your views here.
#crea el rest api view para registarse y que ademas de registrar el user agrege los datos de envio
class RegistroUsuarioView(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            datos_envio_serializer = DatosEnvioSerializer(data=request.data)
            if datos_envio_serializer.is_valid():
                datos_envio = datos_envio_serializer.save(user=user)
                return Response({
                    "user": user_serializer.data,
                    "datos_envio": datos_envio_serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(datos_envio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
