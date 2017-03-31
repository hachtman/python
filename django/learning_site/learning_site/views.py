from django.shortcuts import render


def hello_world(req):
    return render(req, 'home.html')
