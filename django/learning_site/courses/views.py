from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Course


def course_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_show(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_show.html')
