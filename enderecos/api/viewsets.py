from rest_framework import viewsets
from enderecos.api.serializers import EnderecoSerializer

from enderecos.models import Endereco

class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer