from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PackViewSet, new_pack, select_carton, sku_check

router = DefaultRouter()
router.register('orders', PackViewSet)

urlpatterns = [
    path('new-order/', new_pack),
    path('sku-check/', sku_check),
    path('selected-carton/', select_carton),
    path('', include(router.urls)),
]
