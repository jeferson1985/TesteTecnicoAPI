from django.contrib import admin
from sensoriamento.models import EntregaRacao, AlimentacaoSilo

class Entregas(admin.ModelAdmin):
    list_display = ('chave','silo_mac', 'weight_entrega', 'date_entrega', 'hour_initial', 'hour_final', 'duration_entrega',)
    list_display_links = ('chave', 'silo_mac', 'weight_entrega',)
    search_fields = ('chave', 'weight_entrega','silo_mac', 'date_entrega')

class Alimentacao(admin.ModelAdmin):
    list_display = ('silo_mac', 'weight_entrega', 'date_entrega', 'hour_initial', 'hour_final', 'duration_entrega',)
    list_display_links = ('silo_mac', 'weight_entrega',)
    search_fields = ('weight_entrega','silo_mac', 'date_entrega')


admin.site.register(EntregaRacao, Entregas)
admin.site.register(AlimentacaoSilo, Alimentacao)
