from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username=serializers.CharField(required=True)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    phone = serializers.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields=['id','first_name','last_name','username','email','phone','password','confirm_password']

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
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
    


# class SignInSerializer(serializers.Serializer):
#     username=serializers.CharField(required=True)
#     password=serializers.CharField(style={'input_type':"password"})


#     class Meta:
#         model=CustomUser
#         fields=['username','password']
    
