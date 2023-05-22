from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers import UserSerializer, UserLoginSerializer

# 회원가입
class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "회원가입에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)

# 회원 상세정보
class UserDetail(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 회원정보 수정
class UserUpdate(APIView):
    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "회원정보가 수정되었습니다."}, status=status.HTTP_200_OK)
        return Response(data={"message": "회원정보 수정에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)

# 회원찾기
class UserSearch(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 회원탈퇴
class UserDelete(APIView):
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)

# 로그인
class UserLogin(TokenObtainPairView):
    serializer_class = UserLoginSerializer

# 로그아웃
class UserLogout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "로그아웃이 완료되었습니다."}, status=status.HTTP_200_OK)

# 비밀번호 찾기
class UserPasswordFind(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# 비밀번호 변경
class UserPasswordChange(APIView):
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response(data={"message": "비밀번호 변경에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST)


