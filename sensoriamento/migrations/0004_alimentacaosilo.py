# Generated by Django 3.2.9 on 2021-11-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensoriamento', '0003_auto_20211114_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlimentacaoSilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silo_mac', models.CharField(max_length=30)),
                ('weight_entrega', models.FloatField(blank=True, null=True, verbose_name='Peso(kg/s)')),
                ('date_entrega', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('hour_initial', models.TimeField(blank=True, null=True, verbose_name='Hora Inicial')),
                ('hour_final', models.TimeField(blank=True, null=True, verbose_name='Hora Final')),
                ('duration_entrega', models.DurationField(blank=True, null=True, verbose_name='Duração')),
            ],
        ),
    ]
