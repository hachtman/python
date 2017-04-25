from django.test import TestCase
from .models import Course, Step
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.



class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


thing = Course.objects.get(pk=1)


class StepModelTests(TestCase):
    def test_step_creation(self):
        step = Step.objects.create(
            title="Substituions",
            description="Removing stuff and replacing it.",
            course=thing
        )
        now = timezone.now()
        self.assertEqual(step.course, thing)


class CourseViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in python"
        )
        self.course2 = Course.objects.create(
            title="New Course...",
            description="Coming Soon."
        )
        self.step = Step.objects.create(
            title="Introduction to Doctests",
            description="Learn to write tests in your docstrings",
            course=self.course
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.course, response.context['courses'])
        self.assertIn(self.course2, response.context['courses'])
        self.assertTemplateUsed(response, 'courses/course_list.html')
        self.assertContains(response, self.course.title)


        
