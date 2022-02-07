from rest_framework import viewsets
from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer