from rest_framework import viewsets
from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario

class ComentarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
