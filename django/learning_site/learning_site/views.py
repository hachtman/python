from django.shortcuts import render


def hello_world(req):
    print(req, 'THIS IS A REQ TO HELLO WORLD')
    return render(req, 'home.html')
