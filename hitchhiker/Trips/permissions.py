from rest_framework.permissions import BasePermission


class IsOwnerUser(BasePermission):
     
     def has_object_permission(self, request, view, obj):
        if request.method =='PUT' or request.method == 'PATCH' :
                return request.user == obj.username 
     