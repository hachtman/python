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
