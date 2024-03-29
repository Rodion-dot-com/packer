import collections
import os

from django.utils import timezone
from requests import codes, get
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PackSerializer
from yama_pack.models import Pack, RepackingCargotype

YAMA_API_ORDER_DETAILED = os.getenv(
    'YAMA_API_ORDER_DETAILED',
    default='http://127.0.0.1/yama-api/v1/order/'
)
DS_API_PACK = os.getenv(
    'DS_API_PACK',
    default='http://127.0.0.1/pack'
)


def is_required_repacking(cargotypes: list) -> bool:
    return RepackingCargotype.objects.filter(cargotype__in=cargotypes).exists()


@api_view(['POST'])
def new_pack(request):
    orderkey = request.data.get('orderkey')
    sku_count = collections.defaultdict(int)
    for box in request.data.get('boxes'):
        for sku in box.get('skus'):
            sku_count[sku.get('sku').get('sku')] += sku.get('amount')

    items_to_ds = []
    items_to_front = []
    response = get(f'{YAMA_API_ORDER_DETAILED}{orderkey}')
    if response.status_code != codes.ok:
        return Response({'status': 'fail'},
                        status=status.HTTP_400_BAD_REQUEST)
    skus = response.json().get('skus')
    for item in skus:
        sku = item.get('sku')
        if sku_count[sku.get('sku')] > sku.get('num_in_stock'):
            return Response({'status': 'fail'},
                            status=status.HTTP_400_BAD_REQUEST)
        items_to_front.append({
            'sku': sku.get('sku'),
            'amount': sku_count[sku.get('sku')],
            'image': sku.get('image'),
            'description': sku.get('sku_text'),
            'repackaging': is_required_repacking(
                sku.get('cargotype')),
        })
        items_to_ds.append({
            'sku': sku.get('sku'),
            'count': sku_count[sku.get('sku')],
            'size1': sku.get('a'),
            'size2': sku.get('b'),
            'size3': sku.get('c'),
            'weight': sku.get('goods_wght'),
            'type': list(map(str, sku.get('cargotype'))),
        })

    recommendation_response = get(DS_API_PACK, json={
        'orderId': orderkey,
        'items': items_to_ds,
    })
    if recommendation_response.status_code != codes.ok:
        return Response({'status': 'fail'},
                        status=status.HTTP_400_BAD_REQUEST)

    recommended_carton = recommendation_response.json().get(
        'package')[0].get('carton')

    request.session['items'] = sku_count
    request.session['orderkey'] = orderkey

    who = request.data.get('who')
    serializer = PackSerializer(data={
        'orderkey': orderkey,
        'recommended_carton': recommended_carton,
        'who': who,
        'status': 'Собирается',
        'startpack': timezone.now(),
    })
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
