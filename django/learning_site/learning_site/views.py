from django.http import HttpResponse


def hello_world(req):
    print(req)
    return HttpResponse('Hello World')
