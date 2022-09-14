
from payment.models import Payment as PaymentModel
from payment.serializers import PaymentSerializer

def get_payment(payment_id):
    """결제 정보 반환 함수

    Args:
        payment_id (int): 결제 PK

    Returns:
        payment_info (dict): 결제 정보
    """

    payment_obj = PaymentModel.objects.get(id=payment_id)

    payment_info = PaymentSerializer(payment_obj).data

    return payment_info


def create_payment(payment_info):
    """결제 생성 함수

    Args:
        payment_info (dict): 생성할 결제 정보 

    Returns:
        payment_obj (PaymentModel) : 생성된 결제 오브젝트

    """

    payment_serializer = PaymentSerializer(data=payment_info)
    payment_serializer.is_valid(raise_exception=True)
    payment_obj = payment_serializer.save()

    payment_obj.save()

    return payment_obj


def update_payment(payment_id, update_info):
    """결제 정보 수정 함수
    
    Args:
        payment_id (int): 수정할 결제 PK
        update_info (dict): 수정 정보 

    Returns:
        payment_obj (PaymentModel): 수정된 결제 오브젝트

    Raises:
    
    """
    payment_obj = PaymentModel.objects.get(id=payment_id)

    payment_serializer = PaymentSerializer(payment_obj, data=update_info, partial=True)
    payment_serializer.is_valid(raise_exception=True)
    payment_obj = payment_serializer.save()

    return payment_obj


def delete_payment(payment_id):
    """결제 삭제 기능 함수    

    Args:
        payment_id (int): 삭제할 결제 PK
    
    """

    payment_obj = PaymentModel.objects.get(id=payment_id)
    payment_obj.delete()
