from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from payment.services.payment_service import (
    get_payment,
    create_payment,
    update_payment,
    delete_payment
)

# 결제 CRUD View
class PaymentView(APIView):
    # 결제 조회
    def get(self, request, id):
        payment_info = get_payment(id)
        return Response(payment_info, status=status.HTTP_200_OK)

    # 결제 생성
    def post(self, request):
        payment_obj = create_payment(request.data)
        if payment_obj:
            return Response({"success" : "결제 생성 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "결제 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        payment_obj = update_payment(id, request.data)
        if payment_obj:
            return Response({"success" : "결제 정보 수정 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "결제 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        delete_payment(id)
        return Response({"success" : "주문 삭제 성공"}, status=status.HTTP_200_OK)
