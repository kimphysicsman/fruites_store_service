from product.serializers import (
    ProductSerializer,
    PriceSerializer,
)

from product.models import (
    Product as ProductModel,
    Price as PriceModel,
)



def get_product(product_id):
    """상품 정보 반환 함수

    Args:
        product_id (int): 상품 아이디

    Returns:
        product_info (dict): 상품 정보
    """

    product_obj = ProductModel.objects.get(id=product_id)

    product_info = ProductSerializer(product_obj).data

    return product_info


def create_product(product_info):
    """상품 정보로 상품 생성하는 함수

    Args:
        product_info (dict): 생성할 상품 정보 

    Returns:
        product_obj (ProductModel) : 생성된 상품 오브젝트


    """

    product_serializer = ProductSerializer(data=product_info)
    product_serializer.is_valid(raise_exception=True)
    product_obj = product_serializer.save()

    return product_obj


def update_product(product_id, update_info):
    """상품 정보 수정 함수
    
    Args:
        product_id (int): 수정할 상품 PK
        update_info (dict): 수정 정보 

    Returns:
        product_obj (ProductModel): 수정된 상품 오브젝트

    Raises:
    
    """
    product_obj = ProductModel.objects.get(id=product_id)

    product_serializer = ProductSerializer(product_obj, data=update_info, partial=True)
    product_serializer.is_valid(raise_exception=True)
    product_obj = product_serializer.save()

    return product_obj


def delete_product(product_id):
    """상품 삭제 기능 함수    

    Args:
        product_id (int): 삭제할 상품 PK

    Returns:
       
    
    """

    product_obj = ProductModel.objects.get(id=product_id)
    product_obj.delete()


def get_price_list(product_id):
    """ 가격 정보 리스트 반환 함수

    Args:
        product_id (int): 상품 PK

    Returns:
        price_info_list (list): 가격 정보 리스트
    """

    price_obj_list = PriceModel.objects.filter(product__id=product_id)
    
    price_info_list = PriceSerializer(price_obj_list, many=True).data

    return price_info_list


def create_price(product_id, price_info):
    """상품에 대한 가격 생성 함수

    Args:
        product_id (int): 상품 PK
        price_info (dict): 가격 정보

    Returns:
        price_obj (PriceModel): 생성한 가격 오브젝트
    """

    price_info['product'] = product_id
    price_serializer = PriceSerializer(data=price_info)
    price_serializer.is_valid(raise_exception=True)
    price_obj = price_serializer.save()

    return price_obj


def update_price(price_id, update_info):
    """가격 정보 수정 함수
    
    Args:
        price_id (int): 수정할 가격 PK
        update_info (dict): 수정 정보 

    Returns:
        price (PriceModel): 수정된 가격 오브젝트

    Raises:
    
    """
    price_obj = PriceModel.objects.get(id=price_id)

    price_serializer = PriceSerializer(price_obj, data=update_info, partial=True)
    price_serializer.is_valid(raise_exception=True)
    price_obj = price_serializer.save()

    return price_obj    


def delete_price(price_id):
    """가격 삭제 기능 함수    

    Args:
        price_id (int): 삭제할 가격 PK

    Returns:
       
    
    """

    price_obj = PriceModel.objects.get(id=price_id)
    price_obj.delete()
