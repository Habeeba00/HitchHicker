from rest_framework import serializers
from .models import CustomUser,OTP
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    username = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    phone = serializers.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        # Remove the confirm_password key-value pair
        validated_data.pop('confirm_password')

        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    



class RequestPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        token = data.get("token")
        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise serializers.ValidationError("Invalid email address")

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            raise serializers.ValidationError("Invalid or expired token")

        return data
    

class ResetPasswordWithOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')
        new_password = data.get('new_password')

        # Ensure email exists
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email not found.")

        # Ensure OTP matches
        user = CustomUser.objects.get(email=email)
        otp_instance = OTP.objects.filter(user=user, otp=otp).first()
        if not otp_instance:
            raise serializers.ValidationError("Invalid OTP.")

        return data