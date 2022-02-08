from rest_framework import viewsets
from core.models import PontoTuristico
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # http_methods_names = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def get_queryset(self):
        # ctx = super().get_queryset()
        '''Deve retornar um iterable do tipo queryset'''
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        '''Retorna uma lista de objetos'''
        ctx = super().list(request, *args, **kwargs)
        return ctx

    def create(self, request, *args, **kwargs):
        ctx = super().create(request, *args, **kwargs)
        return ctx

    def destroy(self, request, *args, **kwargs):
        ctx = super().destroy(request, *args, **kwargs)
        return ctx

    def update(self, request, *args, **kwargs):
        ctx = super().update(request, *args, **kwargs)
        return ctx

    def partial_update(self, request, *args, **kwargs):
        ctx = super().partial_update(request, *args, **kwargs)
        return ctx

    def retrieve(self, request, *args, **kwargs):
        '''Retorna apenas um objeto'''
        ctx = super().retrieve(request, *args, **kwargs)
        return ctx

    @action(methods=['GET'], detail=True)
    def denunciar(self, request, pk=None):
        '''
            Colocando detail=True, faz com que seja para um recurso específico.
            Se não colocar, será para todos os recursos, e ainda não será passado o pk
            o unico metodo que não vem com data, é o get. os outros vem com data
        '''
        ...