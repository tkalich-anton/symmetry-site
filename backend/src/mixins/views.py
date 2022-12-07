from rest_framework import viewsets

from users.models import CustomUser


class CommonViewSet(viewsets.ModelViewSet):
    """Ensure the models are updated with the requesting user."""

    def perform_create(self, serializer):
        """Ensure we have the authorized user for ownership."""
        user = CustomUser(self.request.user)
        if user:
            serializer.save(created_by=user.id, updated_by=user.id)
        else:
            serializer.save()

    def perform_update(self, serializer):
        """Ensure we have the authorized user for ownership."""
        user = CustomUser(self.request.user)
        print(user)
        if user:
            serializer.save(updated_by=user.id)
        else:
            serializer.save()