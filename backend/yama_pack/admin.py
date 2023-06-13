from django.contrib import admin

from yama_pack.models import Status, Sku, Pack, OrderSku

admin.site.register(Status)
admin.site.register(Sku)
admin.site.register(OrderSku)
admin.site.register(Pack)
