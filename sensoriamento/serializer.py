from django.db.models.fields import files
from rest_framework import serializers
from sensoriamento.models import EntregaRacao, AlimentacaoSilo

class EntregaRacaoSerializer(serializers.ModelSerializer):
    class Meta :
        model = EntregaRacao
        fields = ['chave','silo_mac', 'weight_entrega','date_entrega', 'hour_initial', 'hour_final', 'duration_entrega']


class AlimentacaoSiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlimentacaoSilo
        fields = ['silo_mac', 'weight_entrega','date_entrega', 'hour_initial', 'hour_final', 'duration_entrega']


