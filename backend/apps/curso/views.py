from rest_framework import generics, status
from rest_framework.response import Response

from .models import Curso
from .serializer import CursoSerializer

class ListCreateCurso(generics.ListAPIView):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = CursoSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
