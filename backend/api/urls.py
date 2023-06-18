from django.urls import path

from api.views import new_pack, select_carton, sku_check


urlpatterns = [
    path('new-order/', new_pack),
    path('sku-check/', sku_check),
    path('selected-carton/', select_carton),
]
