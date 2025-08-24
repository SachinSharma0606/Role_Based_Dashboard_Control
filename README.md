# Role based Student Management System Backend using django-restframework

This repository contains the backend code for a **Student Management System** built using the Django REST Framework (DRF). It provides APIs for managing users, students, courses, grades, attendance, and analytics. The system also includes token-based authentication and API documentation using Swagger and ReDoc.

---

## Features

- **User Management**: APIs for user registration and management.
- **Student Records**: CRUD operations for managing student data.
- **Courses and Grades**: APIs to manage courses and student grades.
- **Attendance Tracking**: Attendance management for students.
- **Analytics**: Generate reports and analytics based on student performance.
- **Authentication**: Token-based authentication for secure access.
- **API Documentation**: Swagger and ReDoc for interactive API exploration.

---

## API Endpoints

The following URL patterns are configured in the project:

| Endpoint                  | Description                                  |
|---------------------------|----------------------------------------------|
| `/admin/`                 | Django admin interface.                     |
| `/api/users/`             | User-related operations.                    |
| `/api/students/`          | Student-related operations.                 |
| `/api/courses/`           | Course-related operations.                  |
| `/api/grades/`            | Grade-related operations.                   |
| `/api/attendance/`        | Attendance-related operations.              |
| `/api/analytics/`         | Analytics and reporting endpoints.          |
| `/api/auth/token/`        | Token-based authentication endpoint.        |
| `/swagger/`               | Swagger API documentation.                  |
| `/redoc/`                 | ReDoc API documentation.                    |

---

## Setup and Installation

Follow these steps to set up the backend locally:

### Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework
- SQLlite3

### Installation

Clone the repository:
   git clone https://github.com/Ayushsinghcse/Role-Based-Access-Control-for-School-Colleges.git
   cd student-management-backend

### Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Set up the database:
Configure database settings in settings.py

Run migrations:
python manage.py migrate

Create a superuser for admin access:
python manage.py createsuperuser

### Start the development server:
python manage.py runserver
