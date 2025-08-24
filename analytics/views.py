# analytics/views.py
from rest_framework import generics, permissions
from django.db.models import Count
from .models import APIRequest
from users.models import CustomUser
from courses.models import Course

class MostActiveUsersView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return CustomUser.objects.annotate(request_count=Count('apirequest')).order_by('-request_count')[:10]

class MostPopularCoursesView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return Course.objects.annotate(enrollment_count=Count('enrollment')).order_by('-enrollment_count')[:10]