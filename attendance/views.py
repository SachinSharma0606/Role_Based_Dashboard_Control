# attendance/views.py
from rest_framework import generics, permissions
from .models import Attendance
from .serializers import AttendanceSerializer
import logging

# Set up logger
logger = logging.getLogger(__name__)

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        attendance = serializer.save()
        # Log attendance status (present or absent) for the student in the course on the specified date
        logger.info(f"Attendance marked: {attendance.student} {'present' if attendance.status else 'absent'} in {attendance.course} on {attendance.date}")

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (permissions.IsAuthenticated,)
