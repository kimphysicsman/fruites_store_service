from order.models import (
    Order as OrderModel,
    PriceOrder as PriceOrderModel
    )
from order.serializers import OrderSerializer

from product.models import Price as PriceModel


def get_order(order_id):
    """주문 정보 반환 함수

    Args:
        order_id (int): 주문 PK

    Returns:
        order_info (dict): 주문 정보
    """

    order_obj = OrderModel.objects.get(id=order_id)

    order_info = OrderSerializer(order_obj).data

    return order_info


def create_order(order_info):
    """주문 정보로 주문 생성하는 함수

    Args:
        order_info (dict): 생성할 주문 정보 

    Returns:
        order_obj (OrderModel) : 생성된 주문 오브젝트

    """

    price_id_list = order_info.pop("price", [])

    order_serializer = OrderSerializer(data=order_info)
    order_serializer.is_valid(raise_exception=True)
    order_obj = order_serializer.save()

    for price_id in price_id_list:
        add_price_at_order(order_obj, price_id)

    order_obj.total_price = get_total_price(order_obj)
    order_obj.save()

    return order_obj


def add_price_at_order(order_obj, price_id):
    """주문에 상품 가격 추가 함수

    Args:
        order_obj (OrderModel): 주문 오브젝트
        price_id (PriceModel): 상픔가격 PK

    """

    price_obj = PriceModel.objects.get(id=price_id)

    price_order = PriceOrderModel.objects.create(order=order_obj, price=price_obj)


def delete_price_at_order(order_obj, price_id):
    """주문에 상품 가격 삭제 함수

    Args:
        order_obj (OrderModel): 주문 오브젝트
        price_id (PriceModel): 상픔가격 PK

    """

    price_obj = PriceModel.objects.get(id=price_id)

    price_order = PriceOrderModel.objects.filter(order=order_obj, price=price_obj)

    if len(price_order) != 0:
        price_order.first().delete()


def get_total_price(order_obj):
    """주문의 총 가격 구하는 함수

    Args:
        order_obj (OrderModel): 주문 오브젝트

    Returns:
        (int) : 총 가격
    """
    prices = [ price_obj.price for price_obj in PriceModel.objects.filter(order=order_obj)]

    return sum(prices) + order_obj.delivery_cost


def add_price_and_update_order(order_id, price_id):
    order_obj = OrderModel.objects.get(id=order_id)
        
    add_price_at_order(order_obj, price_id)

    order_obj.total_price = get_total_price(order_obj)
    order_obj.save()

    return order_obj


def delete_price_and_update_order(order_id, price_id):
    order_obj = OrderModel.objects.get(id=order_id)
        
    delete_price_at_order(order_obj, price_id)

    order_obj.total_price = get_total_price(order_obj)
    order_obj.save()

    return order_obj


def update_order(order_id, update_info):
    """주문 정보 수정 함수
    
    Args:
        order_id (int): 수정할 주문 PK
        update_info (dict): 수정 정보 

    Returns:
        order_obj (OrderModel): 수정된 주문 오브젝트

    Raises:
    
    """
    order_obj = OrderModel.objects.get(id=order_id)

    order_serializer = OrderSerializer(order_obj, data=update_info, partial=True)
    order_serializer.is_valid(raise_exception=True)
    order_obj = order_serializer.save()

    order_obj.total_price = get_total_price(order_obj)
    order_obj.save()

    return order_obj



def delete_order(order_id):
    """주문 삭제 기능 함수    

    Args:
        order_id (int): 삭제할 주문 PK
    
    """

    order_obj = OrderModel.objects.get(id=order_id)
    order_obj.delete()
