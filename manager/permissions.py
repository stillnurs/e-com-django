from rest_framework import permissions


class IsVendor(permissions.BasePermission): 
    """
    Only person who has "vendor" status has permission
    """

    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.is_vendor == request.user: 
            return True
        else:
            return False


class IsClient(permissions.BasePermission): 
    """
    Only person who has "client" status has permission
    """

    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.is_client == request.user: 
            return True
        else:
            return False