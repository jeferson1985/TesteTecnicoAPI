from django.db.models import query
from rest_framework import viewsets
from sensoriamento.models import EntregaRacao
from sensoriamento.serializer import EntregaRacaoSerializer, AlimentacaoSilo, AlimentacaoSiloSerializer


class EntregaRacaoViewSet(viewsets.ModelViewSet):
    queryset = EntregaRacao.objects.all()
    serializer_class = EntregaRacaoSerializer

    
class AlimentacaoSiloViewset(viewsets.ModelViewSet):
    queryset = AlimentacaoSilo.objects.all()
    serializer_class = AlimentacaoSiloSerializer