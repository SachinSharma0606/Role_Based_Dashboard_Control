# courses/models.py
from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_taught')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_enrolled', through='Enrollment')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')