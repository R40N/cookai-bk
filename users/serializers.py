from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    # 회원가입    
    def create(self, validated_data):
        user = User.objects.create_user(
            nickname=validated_data['nickname'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
    # 회원정보 수정
    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.save()
        return instance
    
class UserLoginSerializer(TokenObtainPairSerializer):
    # 로그인
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['nickname'] = self.user.nickname
        return data
    
class UserSearchSerializer(serializers.ModelSerializer):
    # 회원찾기
    class Meta:
        model = User
        fields = ['nickname', 'email']
        
class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    # 회원탈퇴
    def delete(self, instance, validated_data):
        instance.delete()
        return instance
    
class UserPasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    # 비밀번호 변경
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
    
class UserPasswordFindSerializer(serializers.ModelSerializer):
    # 비밀번호 찾기
    class Meta:
        model = User
        fields = ['nickname', 'email']
        
class UserPasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    # 비밀번호 초기화
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
