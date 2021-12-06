from vulnman.api import viewsets
from vulnman.api.permission import IsCreatorPermission
from rest_framework.permissions import IsAuthenticated
from apps.projects.api import serializers
from apps.projects import models


class ProjectViewSet(viewsets.CreateListRetrieveViewSet):
    permission_classes = [IsCreatorPermission, IsAuthenticated]
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        return models.Project.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)