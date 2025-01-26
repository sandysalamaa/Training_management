from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Course, Trainer

class CourseModelTest(TestCase):
    def test_course_creation(self):
        trainer = Trainer.objects.create(name="sandy salama", email="sandy@gmail.com")
        course = Course.objects.create(name="celery course", trainer=trainer)
        self.assertEqual(course.name, "celery course")