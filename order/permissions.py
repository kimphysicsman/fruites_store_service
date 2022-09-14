from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from order.models import Order as OrderModel

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsManagerOrIsAuthorOrIsAuthenticatedReadOnly(BasePermission):
    """
    관리자는 모두 가능, 작성자는 본인의 주문에 대해서만 모두 가능, 로그인 사용자는 조회, 생성만 가능
    """
    SAFE_METHODS = ('GET', 'POST')
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.type == "manager":
            return True

        order_id = view.kwargs.get('id', None)

        if order_id:
            try:
                order_author = OrderModel.objects.get(id=order_id).user
            
            except OrderModel.DoesNotExist:
                response ={
                        "detail": "주문을 찾을 수 없습니다.",
                    }
                raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
        else:
            order_author = user

        if user.is_authenticated and order_author == user:
            return True

        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False