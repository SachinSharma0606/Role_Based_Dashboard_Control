# grades/models.py
from django.db import models
from django.conf import settings
from courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.FloatField()
    date = models.DateField(auto_now_add=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades_given')

    class Meta:
        unique_together = ('student', 'course')