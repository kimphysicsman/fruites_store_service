from rest_framework import status, exceptions
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
from product.models import Price as PriceModel

from order.permissions import IsManagerOrIsAuthorOrIsAuthenticatedReadOnly

# 주문 CRUD View
class OrderView(APIView):
    permission_classes = [IsManagerOrIsAuthorOrIsAuthenticatedReadOnly]

    # 주문 조회
    def get(self, request, id):
        try:
            order_info = get_order(id)
            return Response(order_info, status=status.HTTP_200_OK)
        
        except OrderModel.DoesNotExist:
            return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"error": "주문 조회에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 주문 생성
    def post(self, request):
        user_obj = request.user
        if str(user_obj) == "AnonymousUser":
            return Response({"error" : "로그인 해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.data['user'] = user_obj.id

        try:
            order_obj = create_order(request.data)
            return Response({"success" : "주문 생성 성공"}, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "address":
                if error_detail[0].code == "blank":
                    return Response({"error": "배송지가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "배송지는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
                elif error_detail[0].code == "invalid":
                    return Response({"error": "배송지 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "required":
                    return Response({"error": "배송지를 입력해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
            elif error_key == "delivery_cost": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "배송비 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "주문 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "주문 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "주문 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 


            return Response({"error" : "주문 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"error" : "주문 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 주문 수정
    def put(self, request, id):
        try:
            order_obj = update_order(id, request.data)
            return Response({"success" : "주문 정보 수정 성공"}, status=status.HTTP_200_OK)
        
        except OrderModel.DoesNotExist:
            return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "address":
                if error_detail[0].code == "blank":
                    return Response({"error": "배송지가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "배송지는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
                elif error_detail[0].code == "invalid":
                    return Response({"error": "배송지 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "required":
                    return Response({"error": "배송지를 입력해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
            elif error_key == "delivery_cost": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "배송비 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "주문 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "주문 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "주문 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            return Response({"error" : "주문 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"error" : "주문 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            delete_order(id)
            return Response({"success" : "주문 삭제 성공"}, status=status.HTTP_200_OK)

        except OrderModel.DoesNotExist:
            return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"error" : "주문 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)


# 주문에 상품 추가/삭제 View
class OrderPriceView(APIView):
    # 상품가격 추가
    def post(self, request, order_id, price_id):
        try:
            order_obj = add_price_and_update_order(order_id, price_id)
            return Response({"success" : "상품 추가 성공"}, status=status.HTTP_200_OK)
    
        except OrderModel.DoesNotExist:
            return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except PriceModel.DoesNotExist:
            return Response({"error": "상품 가격을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except: 
            return Response({"error" : "상품 추가 실패"}, status=status.HTTP_200_OK)

    # 상품 삭제
    def delete(self, request, order_id, price_id):
        try:
            order_obj = delete_price_and_update_order(order_id, price_id)
            return Response({"success" : "상품 삭제 성공"}, status=status.HTTP_200_OK)
        
        except OrderModel.DoesNotExist:
            return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except: 
            return Response({"error" : "상품 삭제 실패"}, status=status.HTTP_200_OK)
