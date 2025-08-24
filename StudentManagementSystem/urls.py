from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse
from rest_framework.authtoken import views 

# API Documentation Schema
schema_view = get_schema_view(
   openapi.Info(
      title="Student Management System API",
      default_version='v1',
      description="API for Student Management System",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# API Root View
def api_root(request):
    return JsonResponse({"message": "Welcome to the Student Management System API."})

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root),  # Root endpoint
    path('api/users/', include('users.urls')),
    path('api/students/', include('students.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/grades/', include('grades.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/auth/token/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
