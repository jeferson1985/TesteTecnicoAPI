from django.db import models

class EntregaRacao(models.Model):
    chave = models.IntegerField('pk',null=True, blank=True)
    silo_mac = models.CharField(max_length=30)
    weight_entrega = models.FloatField(verbose_name='Peso(kg/s)', null=True, blank=True)
    date_entrega = models.DateField('Data', null = True, blank=True)
    hour_initial = models.TimeField('Hora Inicial', null=True, blank=True)
    hour_final = models.TimeField('Hora Final', null=True, blank=True)
    duration_entrega = models.DurationField('Duração', null=True, blank=True)

    def __srt___(self):
        return self.silo_mac

class AlimentacaoSilo(models.Model):
    silo_mac = models.CharField(max_length=30)
    weight_entrega = models.FloatField(verbose_name='Peso(kg/s)', null=True, blank=True)
    date_entrega = models.DateField('Data', null = True, blank=True)
    hour_initial = models.TimeField('Hora Inicial', null=True, blank=True)
    hour_final = models.TimeField('Hora Final', null=True, blank=True)
    duration_entrega = models.DurationField('Duração', null=True, blank=True)

    def __srt___(self):
        return self.silo_mac