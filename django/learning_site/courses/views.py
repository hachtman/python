from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Course, Step


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    # course = Course.objects.get(pk=pk) Without auto 404 handling
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {"step": step})
