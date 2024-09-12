# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import BlacklistToken  # Assuming BlacklistToken is in the same app
# from rest_framework.exceptions import AuthenticationFailed

# class CustomJWTAuthentication(JWTAuthentication):
#     def get_validated_token(self, raw_token):
#         # Check if the token is blacklisted
#         if BlacklistToken.objects.filter(token=raw_token).exists():
#             raise AuthenticationFailed('This token has been blacklisted.')
#         return super().get_validated_token(raw_token)