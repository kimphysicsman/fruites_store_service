from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from payment.services.payment_service import (
    get_payment,
    create_payment,
    update_payment,
    delete_payment
)

from payment.models import Payment as PaymentModel

# 결제 CRUD View
class PaymentView(APIView):
    # 결제 조회
    def get(self, request, id):
        try:
            payment_info = get_payment(id)
            return Response(payment_info, status=status.HTTP_200_OK)
        
        except PaymentModel.DoesNotExist:
            return Response({"error": "결제를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({"error": "결제 조회에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)


    # 결제 생성
    def post(self, request):
        try:
            payment_obj = create_payment(request.data)
            return Response({"success" : "결제 생성 성공"}, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "price": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "결제 금액 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "method": 
                if error_detail[0].code == "blank":
                    return Response({"error": "결제 방법이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "결제 방법이 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "결제 방법이 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "결제 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "결제 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "결제 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "order":
                if error_detail[0].code == "does_not_exist":
                    return Response({"error": "주문을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND) 
                 
            return Response({"error" : "결제 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "결제 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        try:
            payment_obj = update_payment(id, request.data)
            return Response({"success" : "결제 정보 수정 성공"}, status=status.HTTP_200_OK)
        
        except PaymentModel.DoesNotExist:
            return Response({"error": "결제를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "price": 
                if error_detail[0].code == "invalid":
                    return Response({"error": "결제 금액 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "method": 
                if error_detail[0].code == "blank":
                    return Response({"error": "결제 방법이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "결제 방법이 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "결제 방법이 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "status": 
                if error_detail[0].code == "blank":
                    return Response({"error": "결제 상태가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "결제 상태가 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

                elif error_detail[0].code == "invalid":
                    return Response({"error": "결제 상태 입력 값이 유효하지않습니다."}, status=status.HTTP_400_BAD_REQUEST) 

            return Response({"error" : "결제 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"error" : "결제 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            delete_payment(id)
            return Response({"success" : "결제 삭제 성공"}, status=status.HTTP_200_OK)

        except PaymentModel.DoesNotExist:
            return Response({"error": "결제를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"error" : "결제 삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)