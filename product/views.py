from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from product.servieces.product_service import (
    get_product,    
    create_product,
    update_product, 
    delete_product,

    get_price_list,
    create_price,
    update_price,
    delete_price,
)

# 상품 CRUD View
class ProductView(APIView):
    # 상품 조회
    def get(self, request, id):
        product_info = get_product(id)
        return Response(product_info, status=status.HTTP_200_OK)

    def post(self, request):
        product_obj = create_product(request.data)
        if product_obj:
            return Response({"success" : "상품 생성 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "상품 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        product_obj = update_product(id, request.data)
        if product_obj:
            return Response({"success" : "상품 정보 수정 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "상품 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        delete_product(id)
        return Response({"success" : "상품 삭제 성공"}, status=status.HTTP_200_OK)
        # return Response({"error" : "상품 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)


# 가격 CRUD View
class PriceView(APIView):
    # 가격 조회
    def get(self, request, id):
        price_info_list = get_price_list(id)
        return Response(price_info_list,  status=status.HTTP_200_OK)
    
    def post(self, request, id):
        price_obj = create_price(id, request.data)
        if price_obj:
            return Response({"success" : "가격 생성 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "가격 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        price_obj = update_price(id, request.data)
        if price_obj:
            return Response({"success" : "가격 정보 수정 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "가격 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        delete_price(id)
        return Response({"success" : "가격 삭제 성공"}, status=status.HTTP_200_OK)