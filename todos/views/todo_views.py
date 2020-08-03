from rest_framework import viewsets

from user.permission import IsAdminUser, IsLoggedInUserOrAdmin
from todos.models import Todo
from todos.permission import IsToDoOwner
from todos.serializers import TodoSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsToDoOwner, IsLoggedInUserOrAdmin,)

    def create(self, request, *args, **kwargs):
        request_data = request.data
        request_data['created_by'] = request.user.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if not user.is_anonymous:
            # if not admin
            if user and user.groups_id != "1":
                queryset = queryset.filter(created_by=user)

            return queryset

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]
