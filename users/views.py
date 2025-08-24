# users/views.py
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer
import logging

# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        logger.info(f"New user registered: {user.username}")

# User List View
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

# Logger configuration
logger = logging.getLogger(__name__)
