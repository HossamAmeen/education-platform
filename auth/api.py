from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserAccountSerializer


class RegisterUserAccountAPI(APIView):

    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massage": "User registered successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
