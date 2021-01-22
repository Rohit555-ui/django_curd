from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.apps import apps
user_role_model = apps.get_model('user_info', 'UserRole')

# def admin_only(list_of_role):
#     def decor(view_function):
#         def wrap(request, *args, **kwargs):
#             if 'Admin' in list_of_role:
#                 view_function(request, *args, **kwargs)
#             else:
#                 raise PermissionDenied
#
#         return wrap
#
#     return decor


def decor(view_function):
    def wrap(request, *args, **kwargs):
        a = 11
        if a == 111:
            return view_function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


class DecorClass:
    def __init__(self, view_function):
        self.view_function = view_function

    def __call__(self, request, *args, **kwargs):
        a = 10
        # print("User Name is = "+str(request.user))
        if a == 10:
            return self.view_function(self, request, *args, **kwargs)
        else:
            raise PermissionDenied
