from rest_framework.permissions import BasePermission


class IsOwnerUser(BasePermission):
     
     def has_object_permission(self, request, view, obj):
        print("qqqqqqqqqqqqq")
        if request.method =='PUT' or request.method == 'PATCH' :
                print("dwwqq")
                return request.user == obj.added_by 
     
     
     
     
# class IsCustomUser(BasePermission):
#     """
#     Permission to allow CustomUsers to retrieve all restaurants.
#     """

#     def has_permission(self, request, view):
#         if request.user :
#             # Deny owners from accessing the list of all restaurants
#             if view.action == 'list' and request.user.is_owner:
#                 return False
#             return True
#         return False