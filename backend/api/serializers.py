from rest_framework import serializers

from yama_pack.models import Pack, Status


class PackSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        queryset=Status.objects.all(),
        slug_field='status_name',
    )

    class Meta:
        model = Pack
        fields = ('orderkey', 'status', 'recommended_carton', 'who',
                  'startpack', 'endpack')
