# attendance/models.py
from django.db import models
from django.conf import settings
from courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendance_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'course', 'date')