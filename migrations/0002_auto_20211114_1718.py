# Generated by Django 3.2.9 on 2021-11-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensoriamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregaracao',
            name='datetime_fetched',
        ),
        migrations.RemoveField(
            model_name='entregaracao',
            name='silo_id',
        ),
        migrations.RemoveField(
            model_name='entregaracao',
            name='weight',
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='date_entrega',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='duration_entrega',
            field=models.DurationField(blank=True, null=True, verbose_name='Duração'),
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='hour_final',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Final'),
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='hour_initial',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Inicial'),
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='silo_mac',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entregaracao',
            name='weight_entrega',
            field=models.FloatField(blank=True, null=True, verbose_name='Weight(kg/s)'),
        ),
    ]
