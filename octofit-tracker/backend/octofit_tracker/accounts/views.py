from rest_framework import generics, permissions
from .serializers import UserSerializer
from .models import CustomUser


class CurrentUserView(generics.RetrieveAPIView):
    """Returns the current authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

