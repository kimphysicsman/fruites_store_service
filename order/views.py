from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from order.services.order_service import (
    get_order,
    create_order,
    update_order,
    delete_order,
    add_price_and_update_order,
    delete_price_and_update_order,
)

from order.models import Order as OrderModel

# 주문 CRUD View
class OrderView(APIView):
    # 주문 조회
    def get(self, request, id):
        order_info = get_order(id)
        return Response(order_info, status=status.HTTP_200_OK)
    
    # 주문 생성
    def post(self, request):
        user = request.user
        request.data['user'] = user.id

        order_obj = create_order(request.data)
        if order_obj:
            return Response({"success" : "주문 생성 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "주문 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        order_obj = update_order(id, request.data)
        if order_obj:
            return Response({"success" : "주문 정보 수정 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "주문 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        delete_order(id)
        return Response({"success" : "주문 삭제 성공"}, status=status.HTTP_200_OK)

# 주문에 상품 추가/삭제 View
class OrderPriceView(APIView):
    # 상품가격 추가
    def post(self, request, order_id, price_id):
        order_obj = add_price_and_update_order(order_id, price_id)
        if order_obj:
            return Response({"success" : "상품 추가 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "상품 추가 실패"}, status=status.HTTP_200_OK)

    # 상품 삭제
    def delete(self, request, order_id, price_id):
        order_obj = delete_price_and_update_order(order_id, price_id)
        if order_obj:
            return Response({"success" : "상품 삭제 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "상품 삭제 실패"}, status=status.HTTP_200_OK)
