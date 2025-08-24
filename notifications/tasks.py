# notifications/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from users.models import CustomUser
from courses.models import Course
from grades.models import Grade
from attendance.models import Attendance
from datetime import date, timedelta

@shared_task
def send_daily_attendance_reminder():
    students = CustomUser.objects.filter(role='student')
    for student in students:
        send_mail(
            'Daily Attendance Reminder',
            'Don\'t forget to mark your attendance today!',
            settings.DEFAULT_FROM_EMAIL,
            [student.email],
            fail_silently=False,
        )

@shared_task
def send_grade_update_notification(grade_id):
    grade = Grade.objects.get(id=grade_id)
    send_mail(
        'Grade Update',
        f'Your grade for {grade.course} has been updated to {grade.grade}',
        settings.DEFAULT_FROM_EMAIL,
        [grade.student.email],
        fail_silently=False,
    )

@shared_task
def generate_weekly_report():
    end_date = date.today()
    start_date = end_date - timedelta(days=7)
    
    students = CustomUser.objects.filter(role='student')
    for student in students:
        grades = Grade.objects.filter(student=student, date__range=[start_date, end_date])
        attendance = Attendance.objects.filter(student=student, date__range=[start_date, end_date])
        
        report = f"Weekly Report for {student.username}\n\n"
        report += "Grades:\n"
        for grade in grades:
            report += f"{grade.course}: {grade.grade}\n"
        
        report += "\nAttendance:\n"
        for record in attendance:
            report += f"{record.course} on {record.date}: {'Present' if record.status else 'Absent'}\n"
        
        send_mail(
            'Weekly Performance Report',
            report,
            settings.DEFAULT_FROM_EMAIL,
            [student.email],
            fail_silently=False,
        )