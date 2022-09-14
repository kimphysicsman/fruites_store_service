from django.shortcuts import render

from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from user.services.user_service import (
    get_user,
    create_user,
    update_user,
    delete_user,
)

from user.models import User as UserModel

# 유저 CRUD View
class UserView(APIView):
    # 유저 조회
    def get(self, request, username):
        try:
            user_info = get_user(username)
            return Response(user_info, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({"error": "유저를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": "유저 조회에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

    # 유저 생성
    def post(self, request):
        try:
            user_obj = create_user(request.data)
            return Response({"success" : "유저 생성 성공"}, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "username":
                if error_detail[0].code == "blank":
                    return Response({"error": "아이디가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "max_length":
                    return Response({"error": "아이디를 12글자 이하로 작성해주세요."}, status=status.HTTP_400_BAD_REQUEST)
                elif error_detail[0].code == "unique":
                    return Response({"error": "아이디가 중복되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
            elif error_key == "type":
                if error_detail[0].code == "blank":
                    return Response({"error": "유저 유형이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "유저 유형이 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({"error": "유저 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "유저 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)  
    
    # 유저 정보 수정
    def put(self, request):
        user_obj = request.user
        if str(user_obj) == "AnonymousUser":
            return Response({"error" : "로그인 해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            user_obj = update_user(user_obj, request.data)
            return Response({"success" : "유저 정보 수정 성공"}, status=status.HTTP_200_OK)
        
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "password":
                try:
                    if error_detail.code == "invalid":
                        return Response({"error": str(error_detail)}, status=status.HTTP_400_BAD_REQUEST) 
                except:
                    if error_detail[0].code == "blank":
                        return Response({"error": "비밀번호가 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 

            elif error_key == "type":
                if error_detail[0].code == "blank":
                    return Response({"error": "유저 유형이 빈칸입니다."}, status=status.HTTP_400_BAD_REQUEST) 
                elif error_detail[0].code == "invalid_choice":
                    return Response({"error": "유저 유형이 잘못 선택되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({"error": "유저 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "유저 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)  
    

    # 유저 탈퇴(비활성화)
    def delete(self, request):
        user_obj = request.user
        if str(user_obj) == "AnonymousUser":
            return Response({"error" : "로그인 해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        
        password = request.data.get("password", "")

        try : 
            if delete_user(user_obj, password):
                return Response({"success" : "회원 탈퇴 성공"}, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            error_key = list(e.detail.keys())[0]
            error_detail = e.detail.get(error_key, "")

            if error_key == "password":
                if error_detail.code == "invalid":
                    return Response({"error": str(error_detail)}, status=status.HTTP_400_BAD_REQUEST) 
        
            return Response({"error" : "회원 탈퇴 실패"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error" : "회원 탈퇴 실패"}, status=status.HTTP_400_BAD_REQUEST)