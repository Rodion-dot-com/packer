import collections

from django.utils import timezone
from requests import codes, get
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yama_pack.models import Pack

from api.serializers import PackSerializer

YAMA_API_SKU_DETAILED = 'http://127.0.0.1:8001/yama-api/v1/sku/'
DS_API_PACK = 'http://127.0.0.1:8002/pack/'


def is_required_repacking(cargotypes: list) -> bool:
    return True


@api_view(['POST'])
def new_pack(request):
    orderkey = request.data.get('orderkey')
    sku_count = collections.defaultdict(int)
    for box in request.data.get('boxes'):
        for sku in box.get('skus'):
            sku_count[sku.get('sku').get('sku')] += sku.get('amount')

    items_to_ds = []
    items_to_front = []
    for sku, count in sku_count.items():
        response = get(f'{YAMA_API_SKU_DETAILED}{sku}')
        if response.status_code != codes.ok:
            return Response({'status': 'fail'},
                            status=status.HTTP_400_BAD_REQUEST)
        sku_detail = response.json()
        if count > sku_detail.get('num_in_stock'):
            return Response({'status': 'fail'},
                            status=status.HTTP_400_BAD_REQUEST)
        items_to_front.append({
            'sku': sku,
            'amount': count,
            'image': sku_detail.get('image'),
            'description': sku_detail.get('sku_text'),
            'repackaging': is_required_repacking(sku_detail.get('cargotype')),
        })
        items_to_ds.append({
            'sku': sku,
            'count': count,
            'size1': sku_detail.get('a'),
            'size2': sku_detail.get('b'),
            'size3': sku_detail.get('c'),
            'weight': sku_detail.get('goods_wght'),
            'type': sku_detail.get('cargotype'),
        })

    # recommendation = get(DS_API_PACK, data={
    #     'orderId': orderkey,
    #     'items': items_to_ds,
    # }).json()
    # if recommendation.get('status') != 'ok':
    #     return Response({'status': 'fail'},
    #     status=status.HTTP_400_BAD_REQUEST)
    # recommended_carton = recommendation.get('package')

    request.session['items'] = sku_count
    request.session['orderkey'] = orderkey

    who = request.data.get('who')
    serializer = PackSerializer(data={
        'orderkey': orderkey,
        'recommended_carton': 'YMA',  # recommended_carton
        'who': who,
        'status': 'Собирается',
        'startpack': timezone.now(),
    })
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({
            'status': 'fail'
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'items': items_to_front,
        'status': 'ok',
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def sku_check(request):
    sku = request.data.get('sku')
    if sku not in request.session.get('items'):
        return Response({
            'status': 'fail'
        }, status=status.HTTP_400_BAD_REQUEST)
    request.session.get('items')[sku] -= 1
    if request.session.get('items')[sku] == 0:
        del request.session.get('items')[sku]

    finish = False if request.session.get('items') else True
    request.session.modified = True

    return Response({
        "finish": finish,
        "status": "ok"
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def select_carton(request):
    orderkey = request.session.get('orderkey')

    cur_order = Pack.objects.get(orderkey=orderkey)
    cur_order.selected_carton = request.data.get('selected_carton')
    cur_order.endpack = timezone.now()
    cur_order.save()

    request.session.clear()
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


class PackViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
