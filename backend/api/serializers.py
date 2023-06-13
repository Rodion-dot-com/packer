from rest_framework import serializers
from yama_pack.models import Sku


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = ('id', 'sku')
