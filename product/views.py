from rest_framework import status, exceptions
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

from product.models import (
    Product as ProductModel,
    Price as PriceModel
)

from product.permissions import IsManagerOrIsAuthenticatedReadOnly

# 상품 CRUD View
class ProductView(APIView):
    permission_classes = [IsManagerOrIsAuthenticatedReadOnly]

    # 상품 조회
    def get(self, request, id):
        try:
            product_info = get_product(id)
            return Response(product_info, status=status.HTTP_200_OK)
        
        except ProductModel.DoesNotExist:
            return Response({"error": "상품를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({"error": "상품 조회에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 상픔 생성
    def post(self, request):
        try:
            product_obj = create_product(request.data)
            return Response({"success" : "상품 생성 성공"}, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "name":
                if error_detail[0].code == "blank":
                    return Response({"error": "상품 이름이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "상품 이름은 20글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
                elif error_detail[0].code == "invalid":
                    return Response({"error": "상품 이름 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "required":
                    return Response({"error": "상품 이름을 입력해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

            elif error_key == "description": 
                if error_detail[0].code == "blank":
                    return Response({"error": "상품 설명이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "상품 설명은 200글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "상품 설명 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            
            elif error_key == "address": 
                if error_detail[0].code == "blank":
                    return Response({"error": "판매지가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "판매지는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매지 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "delivery_cost": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "배송비 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "판매 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "판매 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 


            return Response({"error" : "상품 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:    
            return Response({"error" : "상품 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        try:
            product_obj = update_product(id, request.data)
            return Response({"success" : "상품 정보 수정 성공"}, status=status.HTTP_200_OK)
        
        except ProductModel.DoesNotExist:
            return Response({"error": "상품를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "name":
                if error_detail[0].code == "blank":
                    return Response({"error": "상품 이름이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "상품 이름은 20글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
                elif error_detail[0].code == "invalid":
                    return Response({"error": "상품 이름 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST)

            elif error_key == "description": 
                if error_detail[0].code == "blank":
                    return Response({"error": "상품 설명이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "상품 설명은 200글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "상품 설명 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            
            elif error_key == "address": 
                if error_detail[0].code == "blank":
                    return Response({"error": "판매지가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "판매지는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매지 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "delivery_cost": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "배송비 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "판매 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "판매 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            return Response({"error" : "상품 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "상품 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 상품 삭제
    def delete(self, request, id):
        try:
            delete_product(id)
            return Response({"success" : "상품 삭제 성공"}, status=status.HTTP_200_OK)
        
        except ProductModel.DoesNotExist:
            return Response({"error": "상품를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"error" : "상품 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)


# 가격 CRUD View
class PriceView(APIView):
    permission_classes = [IsManagerOrIsAuthenticatedReadOnly]

    # 가격 조회
    def get(self, request, id):
        try:
            price_info_list = get_price_list(id)
            return Response(price_info_list,  status=status.HTTP_200_OK)
        
        except ProductModel.DoesNotExist:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({"error": "상품 가격 조회 실패"}, status=status.HTTP_404_NOT_FOUND)
    
    # 가격 생성
    def post(self, request, id):
        try:
            price_obj = create_price(id, request.data)
            return Response({"success" : "가격 생성 성공"}, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "unit":
                if error_detail[0].code == "blank":
                    return Response({"error": "판매 단위가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "판매 단위는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매 단위 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 
            
                elif error_detail[0].code == "required":
                    return Response({"error": "판매 단위를 입력해야합니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "price":
                if error_detail[0].code == "invalid":
                    return Response({"error": "가격 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

                elif error_detail[0].code == "required":
                    return Response({"error": "가격을 입력해야합니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "stock":
                if error_detail[0].code == "invalid":
                    return Response({"error": "가격 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            return Response({"error" : "가격 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)

        except:    
            return Response({"error" : "가격 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            price_obj = update_price(id, request.data)
            return Response({"success" : "가격 정보 수정 성공"}, status=status.HTTP_200_OK)
        
        except PriceModel.DoesNotExist:
            return Response({"error": "상품 가격을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "unit":
                if error_detail[0].code == "blank":
                    return Response({"error": "판매 단위가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "max_length":
                    return Response({"error": "판매 단위는 100글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "판매 단위 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 
            
                elif error_detail[0].code == "required":
                    return Response({"error": "판매 단위를 입력해야합니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "price":
                if error_detail[0].code == "invalid":
                    return Response({"error": "가격 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

                elif error_detail[0].code == "required":
                    return Response({"error": "가격을 입력해야합니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "stock":
                if error_detail[0].code == "invalid":
                    return Response({"error": "가격 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 
       
            return Response({"error" : "가격 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

        except:    
            return Response({"error" : "가격 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id):
        try:
            delete_price(id)
            return Response({"success" : "가격 삭제 성공"}, status=status.HTTP_200_OK)

        except PriceModel.DoesNotExist:
            return Response({"error": "상품 가격을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except:    
            return Response({"error" : "가격 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)