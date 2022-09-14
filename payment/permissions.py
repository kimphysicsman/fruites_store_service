from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

from payment.models import Payment as PaymentModel

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsManagerOrIsAuthorOrIsAuthenticatedReadOnly(BasePermission):
    """
    관리자는 모두 가능, 작성자는 본인의 결제에 대해서만 모두 가능, 로그인 사용자는 조회, 생성만 가능
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

        payment_id = view.kwargs.get('id', None)
        
        if payment_id:
            try:
                payment_author = PaymentModel.objects.get(id=payment_id).order.user
            
            except PaymentModel.DoesNotExist:
                response ={
                        "detail": "결제을 찾을 수 없습니다.",
                    }
                raise GenericAPIException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
        else:
            payment_author = user


        if user.is_authenticated and payment_author == user:
            return True

        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False