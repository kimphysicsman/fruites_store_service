from rest_framework import serializers

from user.models import User as UserModel
from user.serializers import UserSerializer

def get_user(username):
    """ 
        유저 정보 반환 함수

    Args:
        username (str): 유저 아이디

    Returns:
        user_info (dict) : 유저 정보

    Raises:


    """

    user_obj = UserModel.objects.get(username=username)
    
    user_info = UserSerializer(user_obj).data

    return user_info


def create_user(user_info):
    """ 
        유저 정보로 유저 생성하는 함수

    Args:
        user_info (dict): 생성할 유저 정보 

    Returns:
        user_obj (User) : 생성된 유저 오브젝트


    """

    user_serializer = UserSerializer(data=user_info)
    user_serializer.is_valid(raise_exception=True)
    user_obj = user_serializer.save()

    return user_obj


def update_user(user_obj, update_info):
    """
        유저 정보 수정 함수
    
    Args:
        user_obj (User): 수정할 유저 오브젝트
        update_info (dict): 수정 정보 

    Returns:
        user_obj (User): 수정된 유저 오브젝트

    Raises:
    
    """

    # 현재 비밀번호 일치 여부 확인 코드
    cur_password = update_info.pop("cur_password", None)
    if not user_obj.check_password(cur_password):
        raise serializers.ValidationError(
            detail={"error": "현재 비밀번호가 일치하지 않습니다."},
        )

    # 새로운 비밀번호 수정정보에 추가
    new_password = update_info.pop("new_password", None)
    if new_password:
        update_info["password"] = new_password

    user_serializer = UserSerializer(user_obj, data=update_info, partial=True)
    user_serializer.is_valid(raise_exception=True)
    user_obj = user_serializer.save()

    return user_obj


def delete_user(user_obj, password):
    """회원탈퇴 기능 함수    

    Args:
        user_obj (User): 탈퇴할 유저 오브젝트

    Returns:
        result (bool) : 회원탈퇴(비활성화) 성공 여부
    
    """

    # 현재 비밀번호 일치 여부 확인 코드
    if not user_obj.check_password(password):
        raise serializers.ValidationError(
            detail={"error": "현재 비밀번호가 일치하지 않습니다."},
        )

    user_obj.is_active = False
    user_obj.save()

    return not user_obj.is_active