from rest_framework import permissions


class IsToDoOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, todo_obj):
        return todo_obj.created_by.id == request.user.id


class IsCommentOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, comment_obj):
        return comment_obj.created_by.id == request.user.id


class IsCommentAllowed(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, comment_obj):
        return comment_obj.todo.created_by.id == request.user.id
