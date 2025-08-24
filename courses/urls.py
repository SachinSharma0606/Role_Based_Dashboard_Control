# courses/urls.py
from django.urls import path
from .views import CourseListCreateView, CourseDetailView, EnrollmentListCreateView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
]