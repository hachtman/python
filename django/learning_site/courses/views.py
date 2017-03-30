from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
