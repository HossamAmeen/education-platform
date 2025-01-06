from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.get_role()
        token['email'] = user.email
        return token
