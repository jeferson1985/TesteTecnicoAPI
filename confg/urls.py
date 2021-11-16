from django.contrib import admin
from django.urls import path, include
from sensoriamento.views import EntregaRacaoViewSet, AlimentacaoSiloViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('silo_feed_acquisition', EntregaRacaoViewSet)
router.register('silo_feed_weight', AlimentacaoSiloViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
