from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework import generics
from .tasks import send_verification_email
from rest_framework.permissions import AllowAny
from .models import User


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_verification_email.delay(
                user.id
            )  # Отправляем письмо для подтверждения
            return Response(
                {
                    "message": "User registered successfully! Please verify your email."
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(generics.GenericAPIView):
    queryset = User.objects.all()

    def get(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            user.is_email_verified = True
            return Response({"message": "Email verified successfully"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
