# courses/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass', role='teacher')
        self.course = Course.objects.create(name='Test Course', description='Test Description', instructor=self.user)

    def test_course_creation(self):
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.__str__(), self.course.name)

class CourseViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass', role='teacher')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Test Course', description='Test Description', instructor=self.user)

    def test_get_all_courses(self):
        response = self.client.get(reverse('course-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        data = {'name': 'New Course', 'description': 'New Description', 'instructor': self.user.id}
        response = self.client.post(reverse('course-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)