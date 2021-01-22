from rest_framework import permissions


class IsNameRohit(permissions.BasePermission):
    message = "Name should be only rohit"
    """
    checking name for rohit
    """

    def has_permission(self, request, view):
        name = request.query_params.get("name")
        print("request is")
        print(request.query_params)
        if name == "rohit":
            return True
        else:
            return False


class IsCrudAdmin(permissions.BasePermission):
    """
    permission for crud_admin
    """

    def has_permission(self, request, view):
        authorities = request.data.get("authorities")
        authorities_list = authorities if type(authorities) is list else []
        if "CRUD_ADMIN" in authorities_list:
            return True
        else:
            return False
