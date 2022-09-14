from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.services.user_service import (
    get_user,
    create_user,
    update_user,
    delete_user,
)

# 유저 CRUD View
class UserView(APIView):
    # 유저 조회
    def get(self, request, username):
        user_info = get_user(username)
        return Response(user_info, status=status.HTTP_200_OK)

    # 유저 생성
    def post(self, request):
        user_obj = create_user(request.data)
        if user_obj:
            return Response({"success" : "유저 생성 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "유저 생성 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 유저 정보 수정
    def put(self, request):
        user_obj = request.user
        user_obj = update_user(user_obj, request.data)
        if user_obj:
            return Response({"success" : "유저 정보 수정 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "유저 정보 수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 유저 탈퇴(비활성화)
    def delete(self, request):
        user_obj = request.user
        password = request.data.get("password", "")
        if delete_user(user_obj, password):
            return Response({"success" : "회원 탈퇴 성공"}, status=status.HTTP_200_OK)
        return Response({"error" : "회원 탈퇴 실패"}, status=status.HTTP_400_BAD_REQUEST)