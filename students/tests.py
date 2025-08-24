# students/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass', role='student')
        self.student = Student.objects.create(user=self.user, date_of_birth='2000-01-01')

    def test_student_creation(self):
        self.assertTrue(isinstance(self.student, Student))
        self.assertEqual(self.student.__str__(), self.user.username)

class StudentViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass', role='student')
        self.client.force_authenticate(user=self.user)
        self.student = Student.objects.create(user=self.user, date_of_birth='2000-01-01')

    def test_get_all_students(self):
        response = self.client.get(reverse('student-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        data = {'user': self.user.id, 'date_of_birth': '2000-01-01'}
        response = self.client.post(reverse('student-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)