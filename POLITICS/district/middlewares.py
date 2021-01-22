from django.shortcuts import HttpResponse
# function based middleware
# def my_middleware(get_response):
#     print("One time configuration when server gets started")
#
#     def my_function(request):
#         print(request['a'])
#         print("code before view")
#         response = get_response(request)
#         print("code after view")
#
#         return response
#     return my_function


# class based middleware
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("First time configuration when server gets started")

    def __call__(self, request):
        print("code for each request before the view")
        response = self.get_response(request)
        print("code for each request after the view")
        return response


class MyMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        print("First time configuration when server gets started for MyMiddleware1")

    def __call__(self, request):
        print("code for each request before the view for MyMiddleware1")
        response = self.get_response(request)
        print("code for each request after the view for MyMiddleware1")
        return response


class MyMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print("First time configuration when server gets started for MyMiddleware2")

    def __call__(self, request):
        print("code for each request before the view for MyMiddleware2")
        response = self.get_response(request)
        print("code for each request after the view for MyMiddleware2")
        return response


# def view_func(request, args, kwargs):
#     print("this is process view -- before view")
#     return None


class HooksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("all configuration")

    def __call__(self, request):
        print("1")
        response = self.get_response(request)
        print("2")
        return response

    # def process_view(self, request, args, kwargs):
    #     print("this is process view -- before view")
    #     return HttpResponse("Process view is celled!!!")
    #
    # def process_template_response(self, request, response):
    #     print("this is process view -- before view")
    #     return response



